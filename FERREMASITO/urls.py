from django.urls import path
from .views import home_view

urlpatterns = [
    path('Home.html', home_view),
]
