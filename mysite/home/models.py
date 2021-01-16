from django.db import models
from django.urls import reverse
from django.contrib import admin
import uuid

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    #這邊是去決定數據返回的順序
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    # 個人理解就是他這邊算是一個寫變數的地方，也許html來抓這邊的變數，
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('model-detail-view', args=[str(self.id)])
    
    #定義標準python的類方法__str__，為每個物件返回一個人類可讀的字符串
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # Create your models here.
        record = MyModelName(my_field_name="Instance #1")
        record.save()
        print(record.id) #should return 1 for the first record.
        print(record.my_field_name) # should print 'Instance #1'
        
        # Change record by modifying the fields, then calling save().
        record.my_field_name = "New Instance Name"
        record.save()
        return self.field_name

#書籍類型
class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


#書本資訊模型
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    #書籍類別」(genre)是一個 ManyToManyField ，因此一本書可以有很多書籍類別，而一個書結類別也能夠對應到很多本書
    #ManyToManyField這個就是讓多個class使用
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book_detail', args=[str(self.id)])

class Jackson(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    #date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an author."""
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    favoriteeeee  = models.CharField(max_length=100, default='you need to type something')
    intrest       = models.CharField(max_length=100, default='you need to type something')
    Education     = models.CharField(max_length=100, default='you need to type something')
    #date_of_death = models.DateField('Died', null=True, blank=True)

    #list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_display = ('last_name', 'first_name', 'favoriteeeee' ,'date_of_birth','intrest','Education')
 #   inline = [AuthorInline]
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
#模型管理(ModelAdmin)類別 (他是用來描述排版的)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth','favoriteeeee','intrest','Education')
    #fields = ['first_name', 'last_name',('favoriteeeee','date_of_birth')]
    list_filter = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ('last_name','first_name')
        }),
        ('Availability', {
            'fields': ('date_of_birth', 'favoriteeeee')
        }),
        ('Unavailability', {
            'fields': ('intrest','Education')
        }),
    )

class AuthorAdminInline(admin.TabularInline):
    model = Author
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn')
    fields = ['author', 'genre','isbn','summary' ,'title']
    list_filter = ('title', 'author')
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','imprint','due_back','status')
    list_filter = ('status', 'due_back')

def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

display_genre.short_description = 'Genre'
#執行
#python3 manage.py makemigrations
#python5 manage.py migrate
