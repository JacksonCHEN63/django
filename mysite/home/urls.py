from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('data/', include('home.urls')),
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book'), #views.BookListView.as_view()去調用views.py的BookListView class
    #name=book 是去拿templates base_generic.html的東西
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
#    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
