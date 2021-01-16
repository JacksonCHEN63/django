from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Jackson
from django.views import generic #generic->通用，他可以去調用model的class在database中的資料
from django.shortcuts import get_object_or_404 #函數作為引發Http404異常的快捷方式

#def home(request):
#    return render(request, 'home/index.html')
# Create your views here.

def index(request):
    #這邊Book\BookInstance\Author是去抓models的class
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_jackson = Jackson.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_jackson': num_jackson,
    }
 
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context) 

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'  # Specify your own template name/location
    paginate_by = 10
    def get_context_data(self, **kwargs):
       # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
       # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html' #這行是指定特定的路徑，沒有這一行的話他預設位置會跟create app的名稱相同，＃/home/ubuntu/Django/mysite/templates/home/book_detail.html
    #有指定的話就是/home/ubuntu/Django/mysite/templates/books/book_detail.html
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        return render(request, 'books/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors/author_list.html'
    def get_context_data(self, **kwargs):
       # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
       # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html' #這行是指定特定的路徑，沒有這一行的話他預設位置會跟create app的名稱相同，＃/home/ubuntu/Django/mysite/templates/home/book_detail.html
    #有指定的話就是/home/ubuntu/Django/mysite/templates/books/book_detail.html
    def author_detail_view(request, primary_key):
        try:
            author = Author.objects.get(pk=primary_key)
        except Author.DoesNotExist:
            raise Http404('Author does not exist')
        return render(request, 'authors/author_detail.html', context={'author': author})
