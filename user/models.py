from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField('User Name', max_length=50, default='name')
    last_name = models.CharField('Last Name', max_length=50, default='NaN')
    age = models.SmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user_name} [{self.age}]'
