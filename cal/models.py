from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=10)
    str_addr = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    job_details = models.CharField(max_length=500)
    assignee = models.CharField(max_length=200)
    sched_on = models.DateTimeField('scheduled on')
