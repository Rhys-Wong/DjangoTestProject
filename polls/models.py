from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    questiontext = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Date published:")
    def __str__(self):
        return self.questiontext
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choicetext = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choicetext

class Config(models.Model):
    configname = models.CharField(max_length=100)
    test1 = models.BooleanField(default=0)
    test2 = models.BooleanField(default=0)
    test3 = models.BooleanField(default=0)
    test4 = models.BooleanField(default=0)
    test5 = models.BooleanField(default=0)
    test6 = models.BooleanField(default=0)
    test7 = models.BooleanField(default=0)
    def __str__(self):
        return self.configname