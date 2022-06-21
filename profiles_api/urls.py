from django.urls import path
from profiles_api import views


urlpatterns = [
    path('helloapi/', views.HelloApiView.as_view()),
]
