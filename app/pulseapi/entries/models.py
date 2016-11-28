"""Main entry data"""

from django.db import models

# Create your models here.
class Tag(models.Model):
    """
    Tags used to describe properties of an entry and to
    enable filtering entries by these properties
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class EntryQuerySet(models.query.QuerySet):
    """
    A queryset for entries which returns all entries
    """

    def public(self):
        """
        Return all entries to start
        """
        return self



class Entry(models.Model):
    """
    A pulse entry
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content_url = models.URLField()
    thumbnail_url = models.URLField()
    tags = models.ManyToManyField(
        Tag,
        related_name='entries',
        blank=True,
    )
    objects = EntryQuerySet.as_manager()

    class Meta:
        """
        Make plural not be wrong
        """
        verbose_name_plural = "entries"
        
    def __str__(self):
        return str(self.title)
