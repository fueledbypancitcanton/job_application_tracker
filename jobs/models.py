from django.db import models
from datetime import date

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=30)
    PLATFORM_LIST = [
        ("NONE", "NONE"),
        ("LinkedIn", "LinkedIn"),
        ("Indeed", "Indeed"),
        ("Jobstreet", "Jobstreet")
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_LIST, default="NONE")
    job_title = models.CharField(max_length=50)
    STATUS_LIST = [
        ("NONE", "NONE"),
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Pending Application", "Pending Application"),
        ("Hired", "Hired"),
        ("Rejected", "Rejected"),
        ("Ghosted", "Ghosted")
    ]
    job_status = models.CharField(max_length=30, choices=STATUS_LIST, default="NONE")
    date_applied = models.DateField(("Date"), default=date.today)
    job_link = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name