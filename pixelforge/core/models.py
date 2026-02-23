from django.contrib.auth.models import AbstractUser
from django.db import models

#USer
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('lead', 'Project Lead'),
        ('dev', 'Developer'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#Project
class Project(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    project_lead = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lead_projects',
        limit_choices_to={'role': 'lead'}
    )

    developers = models.ManyToManyField(
        User,
        related_name='dev_projects',
        limit_choices_to={'role': 'dev'},
        blank=True
    )

    def __str__(self):
        return self.name

#Document
class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name