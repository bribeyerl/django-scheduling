from datetime import datetime
import calendar

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views import generic

from .forms import ScheduleForm
from .models import Form


class JobList(generic.ListView):
    model = Form
    # add queryset
    template_name = 'index.html'


class CalendarCreateView(generic.CreateView):
    model = Form
    template_name = 'calendar.html'


def schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = ScheduleForm()
        return render(request, 'schedule.html', {'form': form})
# def schedule(request):
#     if request.method == 'POST':
#         form = ScheduleForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.city = True
#             form.assignee = True
#             form.save()
#     form = ScheduleForm()
# return render(request, 'schedule.html', {'form': form})
# try: return reverse('calendar')
