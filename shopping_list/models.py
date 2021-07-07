from django.db import models

class ItemList(models.Model):
    item = models.TextField()

#creating a users model
#one to many relationship