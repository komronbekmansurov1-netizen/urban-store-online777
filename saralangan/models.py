from django.db import models

# Create your models here.


class Saralangan(models.Model):
   # products = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    joined_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.products