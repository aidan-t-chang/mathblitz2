from django.db import models

# Create your models here.
class Problem(models.Model):
    question = models.TextField()
    answer = models.IntegerField()
    
    def __str__(self):
        return self.question 
 