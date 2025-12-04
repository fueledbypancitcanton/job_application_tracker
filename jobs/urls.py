from django.urls import path
from .views import home, create_job

urlpatterns = [
    path('', home, name="home"),
    path('create/', create_job, name="create"),
]
