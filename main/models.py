from django.db import models

class Task(models.Model):
    title = models.CharField("name", max_length=40)
    text = models.TextField('annotation')
    
    def __str__(self) -> str:
        return self.title
    
    