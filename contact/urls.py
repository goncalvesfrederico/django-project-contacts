from django.urls import path
from contact import views

# create a namespace
app_name = "contact"

urlpatterns = [
    path('', views.index, name='index'),
]
