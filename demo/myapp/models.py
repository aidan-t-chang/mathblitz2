from django.db import models

# Create your models here.
class Problem(models.Model):
    question = models.TextField()
    answer = models.IntegerField()
    wa1 = models.IntegerField(default=1)
    wa2 = models.IntegerField(default=1)
    wa3 = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question 
 