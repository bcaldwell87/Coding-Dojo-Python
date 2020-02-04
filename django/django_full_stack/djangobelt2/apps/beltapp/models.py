from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['first_name']) < 2:
            errors.append("First name is too short")

        if len(post_data['last_name']) < 2:
            errors.append("Last name is too short")

        if not EMAIL_REGEX.match(post_data['email']):
            errors.append("Email is not in the correct format")

        if len(post_data['password']) < 8:
            errors.append("Password is too short")

        if post_data['password'] != post_data['confirm_password']:
            errors.append("Passwords don't match")

        if len(errors) > 0:
            return (False, errors)

        else:
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                password=bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            )
            return (True, new_user)

    def check_login(self, post_data):
        if not EMAIL_REGEX.match(post_data['email']):
            return (False, "Email/Password combination is invalid")
        users_list = self.filter(email=post_data['email'])
        if len(users_list) == 0:
            return (False, "Email/Password combination is invalid")
        else:
            user_obj = users_list[0]
            if bcrypt.checkpw(post_data['password'].encode(),user_obj.password.encode()):
                return (True, user_obj)
            else:
                return (False, "Email/Password combination is invalid")

class WishManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['item']) < 3:
            errors.append("A wish must consist of at least 3 characters")

        if len(post_data['desc']) < 3:
            errors.append("Description must be provided")

        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Wish(models.Model):
    item = models.CharField(max_length=255)
    desc = models.TextField()
    giver = models.ManyToManyField(User, related_name="wish_granted")
    uploader = models.ForeignKey(User, related_name="uploaded_wishes", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item}"

    objects = WishManager()
