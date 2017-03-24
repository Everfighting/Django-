from django.db import models


# Create your models here.
class  Article(models.Model):
    title = models.CharField(max_length=100,default='title')
    content = models.TextField(null=True)
    pub_time = models.DateField(null=True)
    TAG_CHOICES = (
        ('tech','Tech'),
        ('life','Life'),
    )
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)


    def __str__(self):
        return self.title