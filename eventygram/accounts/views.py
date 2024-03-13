from eventygram.accounts.forms import CreateUserForm, UpdateUserForm, LoginUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from eventygram.accounts.models import UserProfile
from django.contrib.auth import login, logout
from django.views import View


class RegisterUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = CreateUserForm()

        return render(request, 'accounts/user_register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('successful_registration', pk=user.pk)

        return render(request, 'accounts/user_register.html', {'form': form})


def successful_registration(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    context = {
        'user': user
    }

    return render(request, 'accounts/successful_registration.html', context)


class LoginUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = LoginUserForm()

        return render(request, 'accounts/user_login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = LoginUserForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('successful_login', pk=user.pk)

        return render(request, 'accounts/user_login.html', {'form': form})


def successful_login(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    context = {
        'user': user
    }

    return render(request, 'accounts/successful_login.html', context)


def logout_user(request):
    logout(request)

    return redirect('login')


def profile_details(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    context = {
        'user': user
    }

    return render(request, 'accounts/profile_details.html', context)


class UpdateUserView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)

        if user == request.user:
            form = UpdateUserForm(instance=user)
            return render(request, 'accounts/profile_update.html', {'form': form})
        else:
            return redirect('profile_details')

    @method_decorator(login_required)
    def post(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)

        if user == request.user:
            form = UpdateUserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile_details', pk=user.pk)
            else:
                return render(request, 'accounts/profile_update.html', {'form': form})
        else:
            return redirect('profile_details')
