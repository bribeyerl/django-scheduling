from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import ScheduleForm
from .models import Form


class JobList(generic.ListView):
    model = Form
    template_name = 'index.html'


def schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = ScheduleForm()

    return render(request, 'schedule.html', {'form': form})
