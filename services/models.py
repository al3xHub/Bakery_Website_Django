from django.db import models


# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True)  # Se añadirá hora cuando se cree por primera vez
    updated = models.DateTimeField(auto_now=True)  # Se ejecuta cada vez que se actualize

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
