from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.liefer_list, name='liefer_list'),
    path('home/', views.liefer_list, name='liefer_list'),
    path('test/', views.test, name='test'),
    path('lieferschein/', views.lieferschein, name='lieferschein'),
    #path(r'^liefer_form_data/$', views.liefer_form_data, name='liefer_form_data'),
    #path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    path('ajax/liefer_form_data/<int:pk>/', views.liefer_form_data, name='liefer_form_data'),
]