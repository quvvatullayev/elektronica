from django.db import models

class Eliments(models.Model):
    key = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.key
    
class Eliment_info(models.Model):
    key = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    eliment = models.ForeignKey(Eliments, on_delete=models.CASCADE)

    def __str__(self):
        return self.key