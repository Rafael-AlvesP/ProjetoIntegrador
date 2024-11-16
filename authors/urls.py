from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('confirm', views.confirm, name='confirm'),
    path('terms', views.terms, name='terms'),
    path("polities", views.polity, name='polities'),
]
