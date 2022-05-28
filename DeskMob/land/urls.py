from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name = 'main'),
    path('ll/', views.looklogs),
    path('ajax_posting1', views.ajax_posting1, name='ajax_posting1'),
    path('ajax_posting2', views.ajax_posting2, name='ajax_posting2'),
    path('create/', views.ReportCreateAPI.as_view(), name='createReport'),
]
