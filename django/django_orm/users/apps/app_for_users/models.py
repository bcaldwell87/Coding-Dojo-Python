from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name} Email: {self.email}"
    
    def say_hello(self):
        return f"Hi my name is {self.name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    fans = models.ManyToManyField(User, related_name="favorite_books")