from django.db import models
# import uuid

#creating a users model (one to many relationship)
# class User(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     #UUIDField is a field for storing universally unique identifiers
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)

class ItemList(models.Model):
    item = models.TextField()
    # id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
