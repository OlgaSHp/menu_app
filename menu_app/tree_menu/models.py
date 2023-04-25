from django.db import models
from django.urls import NoReverseMatch, reverse
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    custom_url = models.CharField(max_length=50, null=True, blank=True)
    url_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_url(self):
        if self.url_name:
            try:
                return reverse(self.url_name)
            except NoReverseMatch:
                return "#"
        elif self.custom_url:
            return self.custom_url
        else:
            return "#"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


