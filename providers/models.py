from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/providers', verbose_name='image', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
