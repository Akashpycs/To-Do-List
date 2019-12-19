from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key = 1)
    task_name = models.CharField(max_length=100)
    task_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30)
    
    def __str__(self):
        return self.task_name
    