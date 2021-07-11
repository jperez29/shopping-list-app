from django.db import models
from django.contrib.auth.models import User


class ItemList(models.Model):
    item = models.TextField()
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.item
