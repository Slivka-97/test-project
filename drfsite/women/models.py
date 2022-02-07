from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
