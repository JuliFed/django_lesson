from django.contrib import admin
from books_app.models import Author, Book, Tag, BooksTags

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BooksTags)


