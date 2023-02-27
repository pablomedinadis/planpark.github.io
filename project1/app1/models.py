from django.db import models

# Create your models here.
class user(models.Model):
    usuario=models.CharField(max_length=50, null=True, blank=True)
    passwd=models.CharField(max_length=50, null=True, blank=True)
    tel=models.CharField(max_length=50, null=True, blank=True)
    mail=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.usuario
        
