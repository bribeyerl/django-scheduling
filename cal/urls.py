from django.urls import path
from . import views
from .views import CalendarCreateView

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('', CalendarCreateView.as_view(), name='calendar'),
]
