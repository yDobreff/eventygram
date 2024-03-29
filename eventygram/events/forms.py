from eventygram.events.widgets import CustomDateSelectWidget
from eventygram.base.choices import PRICE_RANGES
from eventygram.events.models import Event
from eventygram.events import choices
from django.forms import ModelForm
from django import forms


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
            'region',
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


class EventFilterForm(forms.Form):

    price_range = forms.ChoiceField(choices=PRICE_RANGES, required=False)
    type_choices = [('', 'Select Event Type')] + choices.EVENT_TYPES
    type = forms.ChoiceField(choices=type_choices, required=False)
    region_choices = [('', 'Select Region')] + choices.REGIONS
    region = forms.ChoiceField(choices=region_choices, required=False)
