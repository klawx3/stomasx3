from django.urls import path
from .views import view_user

urlpatterns = [
    #user view
    path('', view_user.index),
    path('login', view_user.login),
    path('login_form', view_user.login_form),
    path('register', view_user.register),


]
