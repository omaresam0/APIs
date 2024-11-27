from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    # for a more readable url (null is false after migrating)
    slug = models.SlugField(primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300) 
    pages = models.IntegerField
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.lower().replace(" ", "-")  # Basic slug generation
        super().save(*args, **kwargs)
