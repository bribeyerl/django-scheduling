from datetime import datetime
import calendar

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .forms import ScheduleForm


class LoginView(TemplateView):
    template_name = 'login.html'


class CalendarView(TemplateView):
    template_name = 'calendar.html'


class ScheduleView(View):
    form_class = ScheduleForm
    template_name = 'schedule.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('/calendar/')
        return render(request, self.template_name, {'form': form})

    # def schedule_job(self, request):
    #     if request.method == 'POST':
    #         form = ScheduleForm(request.POST)
    #         if form.is_valid():
    #
    #             return HttpResponseRedirect('/calendar/')
    #
    #     else:
    #         form = ScheduleForm
    #
    #     return render(request, 'schedule.html', {'form': form})
