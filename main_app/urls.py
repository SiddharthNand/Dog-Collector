from django.urls import path
from . import views 
# from dogs.views import DogList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.DogList.as_view(), name='index'),
    path('dogs/<int:dog_id>', views.dogs_detail, name="detail"),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('cats/<int:dog_id>/add_naps/', views.add_naps, name='add_naps'),
]
