from eventygram.events.widgets import CustomDateSelectWidget
from eventygram.events.models import Event
from django.forms import ModelForm


class EventCreationForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_time': CustomDateSelectWidget(),
            'end_time': CustomDateSelectWidget(),
        }


class EventUpdateForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'location',
            'start_time',
            'end_time',
            'type',
            'price',
            'status',
            'image',
        ]

        widgets = {
            'start_time': CustomDateSelectWidget(),
            'end_time': CustomDateSelectWidget(),
        }
