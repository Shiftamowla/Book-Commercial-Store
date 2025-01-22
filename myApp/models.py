from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    auther_link = models.URLField(blank=True, null=True)
    Image=models.ImageField(upload_to='Media/auther_Pic',null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    title_link = models.URLField(blank=True, null=True)
    Image=models.ImageField(upload_to='Media/book_Pic',null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books",null=True)

    def __str__(self):
        return self.title
    
  