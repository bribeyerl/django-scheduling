from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'login.html'


class CalendarView(TemplateView):
    template_name = 'calendar.html'


class ScheduleView(TemplateView):
    template_name = 'schedule.html'
