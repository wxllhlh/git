# -*- coding:utf-8 -*-  
from django.db import models


class Todo(models.Model):
	username = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	description = models.TextField()
	status = models.IntegerField()
	modifytime = models.DateTimeField(auto_now=True)
	class Meta: #修改时间排序
		ordering = ['modifytime']
# Create your models here.
