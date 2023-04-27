from django.db import models

# Create your models here.
class Product(models.Model):
    url=models.URLField() 
    title = models.CharField(max_length=100) 
    ratings=models.IntegerField(blank=True,null=True)
    total_review_count=models.IntegerField(blank=True,null=True)
    website = models.CharField(max_length=100)
    price = models.FloatField() 
    

    def __str__(self):
        return self.title+" "+str(self.url)