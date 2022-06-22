from django.urls import path
from profiles_api import views


urlpatterns = [
    path('hello_api/', views.HelloApiView.as_view()),
]
