from django.forms import ModelForm
from cal.models import Form


class ScheduleForm(ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
