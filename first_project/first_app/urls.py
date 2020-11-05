from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:domain_id>/', views.training, name='domain')

]
