from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from eventygram.accounts.models import UserProfile
from django.forms.widgets import SelectDateWidget


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = [
            'username',
            'password1',
            'password2',
            'email',
        ]


class UpdateUserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)

    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = [
            'age',
            'first_name',
            'last_name',
            'location',
            'phone_number',
            'website',
            'date_of_birth',
            'profile_picture',
        ]

        widgets = {
            'date_of_birth': SelectDateWidget(years=range(1900, 2023)),
        }


class LoginUserForm(AuthenticationForm):
    pass
