from django.urls import path, include
from interview_scheduler.api import views


urlpatterns = [
    path('users/', views.UserRegisterView.as_view(), name="users"),
    path('time_slots/', views.ScheduleView.as_view(), name="time_slots")
]