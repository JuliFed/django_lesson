from django.db import models


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author__isnull=False)

    def with_tags(self, tag):
        return self.get_queryset().filter(tags__name=tag)


class Author(models.Model):
    name = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books', through='BooksTags')
    object = models.Manager()
    with_author = BookManager()
    # в выборке Book.with_author.filter()


class BooksTags(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='book_tags')




