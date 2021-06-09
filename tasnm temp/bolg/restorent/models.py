from django.db import models

# Create your models here.

class BlogMOdel(models.Model):
    name=models.CharField(max_length=100, null=True)
    lastname=models.CharField(max_length=100,null=True)
    contect=models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'blogmaster'
        