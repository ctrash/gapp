from django.urls import path
from . import views

urlpatterns = [
    path('', views.liefer_list, name='liefer_list'),
    path('home/', views.liefer_list, name='liefer_list'),
    path('test/', views.test, name='test'),
    path('lieferschein/', views.lieferschein, name='lieferschein'),

]