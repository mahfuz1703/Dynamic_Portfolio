from django.db import models

# Create your models here.
class About(models.Model):
    description = models.TextField(max_length=1000, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gmail = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    degree = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    fromYear = models.CharField(max_length=10, blank=True)
    toYear = models.CharField(max_length=10, blank=True)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.degree

class Experience(models.Model):
    designation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    fromYear = models.CharField(max_length=100, blank=True)
    toYear = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.company