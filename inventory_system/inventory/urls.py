from django.urls import path
from .views import RegisterUser, ItemListCreate, ItemDetail


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('items/',ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/',ItemDetail.as_view(), name='item-detail'),
]