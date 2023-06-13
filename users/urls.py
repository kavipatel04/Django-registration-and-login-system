from django.urls import path
from .views import home, profile, RegisterView, submit_points, verify_points



urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('points/', submit_points, name='users-points'),
    path('verification/', verify_points, name='users-verifications'),
]
