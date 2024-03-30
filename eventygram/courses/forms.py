from eventygram.courses.choices import STUDY_METHODS, COURSE_LANGUAGES, COURSE_LEVELS
from eventygram.base.choices import PRICE_RANGES
from eventygram.courses.models import Course
from django.forms import ModelForm
from django import forms


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseUpdateForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'status',
            'title',
            'topic',
            'language',
            'price',
            'location',
            'study_method',
            'level',
            'requirements',
            'description',
            'content',
            'image',
            'subcategory',
        ]


class CourseFilterForm(forms.Form):
    study_method = forms.ChoiceField(
        label='Study Method',
        choices=[('', 'Select Study Method')] + STUDY_METHODS,
        required=False,
    )

    price_range = forms.ChoiceField(
        label='Price Range',
        choices=PRICE_RANGES,
        required=False,
    )

    language = forms.ChoiceField(
        label='Language',
        choices=[('', 'Select Language')] + COURSE_LANGUAGES,
        required=False,
    )

    level = forms.ChoiceField(
        label='Level',
        choices=[('', 'Select Level')] + COURSE_LEVELS,
        required=False,
    )