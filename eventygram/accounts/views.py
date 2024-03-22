from django.contrib.auth import login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from eventygram.accounts.forms import CreateProfileForm, UpdateProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from eventygram.accounts.models import ProfileSubscriber
from django.contrib import messages
from django.views import View


class CreateProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = CreateProfileForm()

        return render(request, 'accounts/profile_register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = CreateProfileForm(request.POST)

        if form.is_valid():
            new_profile = form.save(commit=False)
            profile_type = form.cleaned_data['profile_type']
            new_profile.profile_type = profile_type
            new_profile.save()
            login(request, new_profile)

            return redirect('successful_registration', pk=new_profile.pk)

        return render(request, 'accounts/profile_register.html', {'form': form})


class LoginProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = AuthenticationForm()

        return render(request, 'accounts/profile_login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            profile = form.get_user()

            if profile.groups.exists():
                profile.is_staff = True

            profile.save()

            login(request, profile)
            return redirect('successful_login', pk=profile.pk)

        return render(request, 'accounts/profile_login.html', {'form': form})


@login_required
def logout_profile(request):
    logout(request)

    return redirect('profile_login')


@login_required
def change_password(request, pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('successful_password', pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def profile_details(request, pk):
    profile_model = get_user_model()
    profile = get_object_or_404(profile_model, pk=pk)

    profile_group = None
    is_subscribed = None

    if profile.groups.exists():
        profile_group = profile.groups.first().name[:-1]
    elif profile.is_superuser:
        profile_group = "Admin"

    if request.user.is_authenticated:
        is_subscribed = ProfileSubscriber.objects.filter(subscriber=request.user, subscribed_to=profile).exists()

    context = {
        'profile': profile,
        'profile_group': profile_group,
        'is_subscribed': is_subscribed,
    }

    return render(request, 'accounts/profile_details.html', context)


class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        profile_model = get_user_model()
        profile = get_object_or_404(profile_model, pk=pk)

        if profile.pk == request.user.pk:
            form = UpdateProfileForm(instance=profile)
            return render(request, 'accounts/profile_update.html', {'form': form, 'profile': profile})
        else:
            return redirect('profile_details', pk=request.user.pk)

    def post(self, request, pk):
        profile_model = get_user_model()
        profile = get_object_or_404(profile_model, pk=pk)

        if profile == request.user:
            form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile_details', pk=profile.pk)
            else:
                return render(request, 'accounts/profile_update.html', {'form': form})
        else:
            return redirect('profile_details', pk=request.user.pk)


@login_required
def add_balance(request, pk):
    profile_model = get_user_model()
    profile = get_object_or_404(profile_model, pk=pk)

    context = {
        'profile': profile
    }

    return render(request, 'accounts/add_balance.html', context)


@login_required
def subscribe_profile(request, pk):
    profile = get_user_model()

    if request.method == 'POST':
        profile_to_subscribe = get_object_or_404(profile, pk=pk)
        current_user = request.user

        if current_user.pk == profile_to_subscribe.pk:
            return redirect('profile_details', pk=pk)

        subscription_exists = ProfileSubscriber.objects.filter(subscriber=current_user,
                                                               subscribed_to=profile_to_subscribe).exists()
        if not subscription_exists:
            ProfileSubscriber.objects.create(subscriber=current_user, subscribed_to=profile_to_subscribe)

        return redirect('profile_details', pk=pk)


@login_required
def unsubscribe_profile(request, pk):
    profile = get_user_model()

    if request.method == 'POST':
        profile_to_unsubscribe = get_object_or_404(profile, pk=pk)
        current_user = request.user

        subscription = ProfileSubscriber.objects.filter(subscriber=current_user,
                                                        subscribed_to=profile_to_unsubscribe).first()
        if subscription:
            subscription.delete()

        return redirect('profile_details', pk=pk)


def profile_events(request, pk):
    profile_model = get_user_model()
    profile = get_object_or_404(profile_model, pk=pk)
    events = profile.event_creator.all()

    context = {
        'events': events,
    }

    return render(request, 'accounts/my_events.html', context)


def profile_courses(request, pk):
    profile_model = get_user_model()
    profile = get_object_or_404(profile_model, pk=pk)
    courses = profile.course_creator.all()

    context = {
        'courses': courses,
    }

    return render(request, 'accounts/my_courses.html', context)
