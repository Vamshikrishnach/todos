from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.
class Task1(models.Model):
    task_name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField()
    
    def __str__(self):
        return self.task_name

class TaskCompletionstatus(models.Model):
    COMPLETION_CHOICES = [
        ('completed', 'Completed'),
        ('uncompleted', 'Uncompleted'),
    ]
    completed_status = models.ForeignKey(Task1, on_delete=models.CASCADE, related_name='completions')
    is_completed = models.CharField(max_length=20, choices=COMPLETION_CHOICES, default='uncompleted')

    def __str__(self):
        completion_status_str = f'{self.completed_status.task_name} - {self.is_completed}'
        return completion_status_str
    


class TaskCreator(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created_tasks = models.ManyToManyField(Task1, related_name='creators')

    def __str__(self):
        return self.user.username
