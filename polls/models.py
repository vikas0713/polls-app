from django.db import models

# Create your models here.


class Poll(models.Model):
    """Polls models """
    title = models.CharField(max_length=255, default='')
    rating = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
