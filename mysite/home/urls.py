from django.urls import include, path
from . import views

app_name = 'Chanth'
urlpatterns = [
    path('', views.homepage, name='Acceuil'),
    path('about/', views.about, name='about'),
    path('tarif/', views.tarif, name='tarif'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agenda/', views.user_agenda, name='user_agenda'),
]
