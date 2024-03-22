from eventygram.courses.models import Course
from django import forms


class CourseCreateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
