from django.shortcuts import render, redirect
from django.views import View
from eventygram.base.forms import ContactForm


def index(request):
    return render(request, 'base/index.html')


def about(request):
    return render(request, 'base/about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm()

        return render(request, 'base/contacts.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            # Handle valid form submission here
            return redirect('successful_message')

        return render(request, 'base/contacts.html', {'form': form})


def profile(request):
    user = request.user

    return redirect('profile_details', pk=user.pk)


def successful_message(request):
    return render(request, 'base/successful_message.html')

