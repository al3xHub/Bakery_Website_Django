from django.urls import path
from . import views

urlpatterns = [
    #  Paths de Contact
    path('', views.contact, name="contact")
]
