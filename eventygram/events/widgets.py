from django.forms import SelectDateWidget
from django.utils import timezone


class CustomDateSelectWidget(SelectDateWidget):
    def __init__(self, *args, **kwargs):
        super(CustomDateSelectWidget, self).__init__(*args, **kwargs)
        self.years = range(timezone.now().year, timezone.now().year + 10)
