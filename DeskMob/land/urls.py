from . import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('ll/', views.looklogs)
]