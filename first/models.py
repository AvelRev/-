from django.db import models
from django.contrib.auth.models import User

class LogEntry(models.Model):
    date = models.DateField()
    time = models.TimeField()
    input_string = models.TextField()
    word_count = models.IntegerField()
    number_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='log_entries')  # добавлен related_name

    def __str__(self):
        return f"{self.user} - {self.input_string} - {self.date} {self.time}"