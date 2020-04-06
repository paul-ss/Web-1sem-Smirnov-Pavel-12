# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
import pytz


# Model managers

class QuestionManager(models.Manager):
    def new_questions(self):
        return self.order_by("-creation_date")


    def hot_questions(self):
        return self.filter(rating__gt=0).order_by("-rating")


    def tag_questions(self, tag_name):
        if (tag_name == None):
            return None
        else:
            return self.filter(tags__name__exact = tag_name)


    def pk_question(self, pk):
        try:
            question =  self.get(pk = pk)
        except Question.DoesNotExist:
            question = None
        return question


    # def create_draft(self, **kwargs):
    #     kwargs['draft'] = True
    #     return self.create(**kwargs)



class AnswerManager(models.Manager):
    def get_answers(self, question):
        return self.filter(question = question).order_by("-rating")








# Models

    #on_delete - что делать, если удалили тот объект, на который ссылались

class Question(models.Model):
    title = models.TextField(default = "")
    #title = models.CharField(max_length=255)
    description = models.TextField(default = "")
    creation_date = models.DateTimeField(blank=True, default = timezone.now)
    rating = models.IntegerField(default = 0)


    #relations
    tags = models.ManyToManyField('Tag')
    profile = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL) #??????
    likes = GenericRelation('Like', related_query_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return self.title




class Answer(models.Model):
    description = models.TextField(default = "")
    is_correct = models.BooleanField (default = False)
    creation_date = models.DateTimeField(blank=True, default = timezone.now)
    rating = models.IntegerField(default = 0)

    profile = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL) #??????
    question = models.ForeignKey('Question', null=True, on_delete=models.CASCADE) #??????
    likes = GenericRelation('Like', related_query_name='answers')

    objects = AnswerManager()

    def __str__(self):
        return self.description



class Tag(models.Model):
    name = models.CharField(max_length=128)

    #relations
    #question = models.ManyToManyField(Question) #??

    def __str__(self):
        return self.name




class Profile(models.Model):
    avatar = models.TextField(default = "")

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username




class Like(models.Model):
    like = models.IntegerField(default = 0)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, null = True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey()

    def __str__(self):
        return str(self.like)
