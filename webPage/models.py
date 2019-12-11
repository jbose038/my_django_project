# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User,on_delete=True, null=True, default=1)
	body = RichTextUploadingField()

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=True, null=True)
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_user = models.TextField(max_length=20)
	comment_thumbnail_url = models.TextField(max_length=300)
	comment_textfield = models.TextField()

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=timezone.now())
	#put_date = models.DateTimeField(auto_now_add=True)


	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	#was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)