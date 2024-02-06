from django.db import models


# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True)  # Unique es como un id que siempre es único.
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # Se añadirá hora cuando se cree por primera vez
    updated = models.DateTimeField(auto_now=True)  # Se ejecuta cada vez que se actualize

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
        ordering = ['name']

    def __str__(self):
        return self.name
