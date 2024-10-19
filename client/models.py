from django.db import models
import uuid


class Client (models.Model):
    mobile = models.CharField(max_length=13)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    create_at = models.DateTimeField(auto_now_add=True)
    answer = models.IntegerField(default=0)
    gift = models.CharField(max_length=250 , null= True)

    def __str__(self) :
        return self.mobile