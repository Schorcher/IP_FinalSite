from django.db import models

# Create your models here.


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=255)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=255)


class Page(models.Model):
    title = models.CharField(max_length=255)


