from django.db import models

# Create your models here.

class UserModel(models.Model):
    full_name = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    role_name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.full_name
    

