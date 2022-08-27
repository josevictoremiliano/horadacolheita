from django.db import models

# Create your models here.

class Feirantes(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class ItensFeira(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='itens', blank=True, null=True)
    feirante = models.ForeignKey(Feirantes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name