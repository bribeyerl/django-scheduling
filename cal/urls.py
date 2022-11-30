from django.urls import path
from . import views
from .views import CalendarCreateView

urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('calendar/', CalendarCreateView.as_view(), name='calendar'),
]
