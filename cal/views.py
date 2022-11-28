from datetime import datetime
import calendar

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView

from .forms import ScheduleForm
from .models import Form


class CalendarCreateView(CreateView):
    model = Form
    template_name = 'calendar.html'
    fields = [
        'assignee',
        'city'
    ]


def schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.city = True
            form.assignee = True
            form.save()
    form = ScheduleForm()
    return render(request, 'schedule.html', {'form': form})