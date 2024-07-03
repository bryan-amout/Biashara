
from django.contrib import admin
from django.urls import path
from Biasharaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('about/', views.About),
    path('contact/', views.Contact),
]
