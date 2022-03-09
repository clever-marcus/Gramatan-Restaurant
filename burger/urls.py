from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('speciality/', views.speciality, name="speciality"),
    path('popular/', views.popular, name="popular"),
    path('gallery/', views.gallery, name="gallery"),
    path('review/', views.review, name="review"),
    path('checkout/', views.checkout, name="checkout"),
    path('order/', views.order, name="order"),
]