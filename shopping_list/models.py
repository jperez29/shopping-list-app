from django.db import models
from django.contrib.auth.models import User
# import uuid

#creating a users model (one to many relationship)
# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(primary_key=True)

#     def __str__(self):
#         return f"<{self.first_name} {self.last_name}>"
    # email = models.CharField(primary_key = True, max_length=30)
#     #UUIDField is a field for storing universally unique identifiers
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)

class ItemList(models.Model):
    item = models.TextField()
    # id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.item
