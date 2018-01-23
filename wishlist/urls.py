from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('Home', views.HomePage.as_view(), name= 'home'),
    path('wish/<int:pk>/', views.WishDetailView.as_view(), name='wish_detail'),
    path('wish/new/', views.WishCreateView.as_view(), name='wish_new'),
    path('wish/<int:pk>/edit/',views.WishUpdateView.as_view(), name='wish_edit'),
    path('wish/<int:pk>/delete/',views.WishDeleteView.as_view(), name='wish_delete'),
    path('wishes/',views.WishListView.as_view(), name='show_wishes'),
]