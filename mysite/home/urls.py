from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('home/', include('home.urls')),
    path('', views.home),
]
