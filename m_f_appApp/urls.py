from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/edit/<int:id>/', views.edit_contact, name='edit'),
    path('contact/delete/<int:id>/', views.delete_contact, name='delete'),
]
