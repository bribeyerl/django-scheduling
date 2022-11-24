from django.urls import path
from .views import ScheduleView, CalendarView, LoginView

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('', LoginView.as_view(), name='login'),
]
