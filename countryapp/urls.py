from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),  
    path('countries-list/', views.countries_list, name='countries_list'),  
    path('country/<str:country_name>/', views.country_detail, name='country_detail'),  
    path('languages/', views.languages_list, name='languages_list'),  
    path('language/<str:language_name>/', views.language_detail, name='language_detail'),  
]