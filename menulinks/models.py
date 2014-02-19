from django.db import models

class MenuLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
