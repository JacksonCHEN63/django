from django.contrib import admin
from .models import Author, Genre, Book, BookInstance,Author2,AuthorAdmin,BookAdmin,BookInstanceAdmin

#admin.site.register(Book)
admin.site.register(Book,BookAdmin)
#admin.site.register(Author)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Author2)
admin.site.register(Genre)
admin.site.register(BookInstance,BookInstanceAdmin)
# Register your models here.
