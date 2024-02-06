from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    order = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)  # Se añadirá hora cuando se cree por primera vez
    updated = models.DateTimeField(auto_now=True)  # Se ejecuta cada vez que se actualize

    class Meta:
        verbose_name = 'web'
        verbose_name_plural = 'websites'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
