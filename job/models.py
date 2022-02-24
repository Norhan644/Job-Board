from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full_Time', 'Full_Time'),
    ('Part_Time', 'Part_Time'),
)

GENDET_TYPE = (
    ('Femel', 'Femel'),
    ('Male', 'Male'),
    ('Prefer not answer', 'Prefer not to answer'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_time = models.CharField(max_length=15, choices = JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, choices=GENDET_TYPE)
    #category


    def __str__(self):
        return self.title

