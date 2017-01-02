from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.db.models.aggregates import Count
from random import randint

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)

	'''def was_published_recently(self):
		now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now'''

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.IntegerField(default=0)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.IntegerField(default=0)

class Student(models.Model):
	name = models.CharField(max_length=200)
	
class Test(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	test_time = models.DateTimeField(auto_now_add=True, blank=True)
	score = models.IntegerField(default=0)

class Count(models.Model):
	count = models.IntegerField(default=0)
	score_value = models.IntegerField(default=0)
