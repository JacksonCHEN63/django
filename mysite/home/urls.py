from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('data/', include('home.urls')),
    path('', views.index, name='index'),
#    path('books/', views.BookListView.as_view(), name='books'),
#    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
#    path('admin/', admin.site.urls),
]
