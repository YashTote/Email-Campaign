from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_email),
    path('add_user/', views.add_user),
    path('edit_user_status/', views.edit_user_status),
]