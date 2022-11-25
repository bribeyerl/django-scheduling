from django.forms import ModelForm
from cal.models import Form

class ScheduleForm(ModelForm):
    class Meta:
        model = Form
        fields = ['first_name', 'last_name', 'phone_num', 'str_addr', 'city', 'zip', 'job_details', 'assignee', 'sched_on']
