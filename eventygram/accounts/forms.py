from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import SelectDateWidget
from eventygram.accounts.models import Profile


class CreateProfileForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile

        fields = [
            'profile_type',
            'username',
            'password1',
            'password2',
            'email',

        ]


class UpdateProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = [
            'is_private',
            'email',
            'first_name',
            'last_name',
            'location',
            'phone_number',
            'website',
            'date_of_birth',
            'profile_picture',
            'bio',
            'industry',  # company field
            'address',  # company field
            'description',  # company field
            'type',  # organization filed
            'mission',  # organization field
        ]

        widgets = {
            'date_of_birth': SelectDateWidget(years=range(1900, 2023)),
            'phone_number': forms.TextInput(attrs={'placeholder': '+'}),
            'is_private': forms.RadioSelect(
                choices=(
                    (True, 'Private'),
                    (False, 'Public')
                )
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)