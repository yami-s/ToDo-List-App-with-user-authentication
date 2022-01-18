from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    creation_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    class Meta:
        order_with_respect_to = 'user'