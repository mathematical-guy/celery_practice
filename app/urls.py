from django.urls import path
from .views import generate_users, users



urlpatterns = [
    path('generate/', generate_users, name='generate'),
    path('users/', users,name='users')
]
