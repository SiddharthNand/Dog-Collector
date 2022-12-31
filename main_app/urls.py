from django.urls import path
from . import views 
# from dogs.views import DogList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.DogList.as_view(), name='index'),
    path('dogs/<int:dog_id>', views.dogs_detail, name="detail"),
    path('cats/create/', views.DogCreate.as_view(), name='dogs_create')
]
