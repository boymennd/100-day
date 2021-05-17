from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.contact, name='contact'),
    path('get_contact/', views.get_contact, name='get_contact')
]