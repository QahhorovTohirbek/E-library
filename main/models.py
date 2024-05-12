from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg



class User(AbstractUser):
    place = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Press(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    career = models.TextField()
    place = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)


    def __str__(self):
        return self.name
    

    @property
    def books(self):
        return Book.objects.filter(author=self)


class Book(models.Model):
    AVAILABLE = 'Available'
    READING = 'Reading'
    FINISHED = 'Finished'

    BOOK_STATUS_CHOICES = [
        (1, AVAILABLE),
        (2, READING),
        (3, FINISHED),
    ]

    book_status = models.IntegerField(choices=BOOK_STATUS_CHOICES)
    name = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to='photos/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    press = models.ForeignKey(Press, on_delete=models.CASCADE)

    paper_book = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ebook = models.CharField(max_length=255, null=True, blank=True)
    audio_book = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    
    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        average_rating = self.book.review_set.all().aggregate(Avg('rating'))['rating__avg']

        if average_rating is not None:
            self.rating = average_rating
        else:
            self.rating = 0
        
        self.book.save()


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.book.name
    


