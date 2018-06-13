from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books', through='BooksTags')


class BooksTags(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='book_tags')




