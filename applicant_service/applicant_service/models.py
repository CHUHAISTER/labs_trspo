from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    intake_capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    certificate_score = models.FloatField()


