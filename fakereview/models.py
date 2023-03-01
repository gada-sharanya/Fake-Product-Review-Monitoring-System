from django.db import models

from django.db.models import Model

class RegistrationModel(Model):

    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

class ProductModel(models.Model):

    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    manufacturer=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.FileField(upload_to="products")

class CommentModel(models.Model):

    text = models.TextField(max_length=5000)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.CharField(max_length=60)
    product = models.CharField(max_length=60)
    istruthfull=models.CharField(max_length=60)

class SearchHistoryModel(models.Model):

    keyword = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.CharField(max_length=60)

class LikeOrDisLikeModel(models.Model):

    status = models.CharField(max_length=100)
    user = models.CharField(max_length=60)
    product = models.CharField(max_length=60)

class TransactionModel(models.Model):

    userid=models.CharField(max_length=100)
    productid=models.CharField(max_length=100)
    tdate=models.DateTimeField(auto_now=True, blank=False, null=False)
    status = models.CharField(max_length=100)