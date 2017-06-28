from django.db import models

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Jobs(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=1000)
    expmax=models.IntegerField()
    skillset=models.ManyToManyField(Skill)

    def __str__(self):
        return self.name



