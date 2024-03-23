from eventygram.courses.models import Course
from django.forms import ModelForm


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
