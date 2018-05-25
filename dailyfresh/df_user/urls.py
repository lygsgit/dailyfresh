from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register),
    path('register_handle/', views.register_handle),
    path('register_exist/', views.register_exist),

]