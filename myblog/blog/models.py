from django.db import models

# Create your models here.
class  Article(models.Model):
    title = models.CharField(max_length=100,default='title')
    content = models.TextField(null=True)
    pub_time = models.DateField(null=True)

    def __str__(self):
        return self.title