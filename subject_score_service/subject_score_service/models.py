from django.db import models
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    intake_capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    certificate_score = models.FloatField()
class SubjectScore(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.applicant.name} - {self.subject.name}: {self.score}"