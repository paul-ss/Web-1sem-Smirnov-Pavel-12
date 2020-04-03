# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response  #optional

from django.http import HttpResponse
import random
from django.core.urlresolvers import reverse
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator

from blog.models import *


def paginate(objects_list, request, per_page):
    page_number = request.GET.get('page')
    if (page_number == None):
        page_number = 1

    paginator = Paginator(objects_list, per_page)
    if (paginator.num_pages == 0):
        return None, None

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except InvalidPage:
        page = paginator.page(1)

    return page.object_list, page




def hello(request):
    return HttpResponse(reverse('hello'))




def index(request):
    tittle = "index"

    question_list = Question.objects.new_questions()
    question_list_current_page, page = paginate(question_list, request, 5)

    return render_to_response('index.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
    })




def hot(request):
    tittle = 'hot'

    question_list = Question.objects.hot_questions()
    question_list_current_page, page = paginate(question_list, request, 5)

    return render_to_response('hot.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
    })



def tag(request, tag = None):
    tittle = "tag: " + tag

    question_list = Question.objects.tag_questions(tag)
    question_list_current_page, page = paginate(question_list, request, 5)

    return render_to_response('tag.html', {
        'tag' : tag,
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
    })



def question(request, id = None):
    tittle = "question: " + id

    question = Question.objects.pk_question(id)
    answer_list = Answer.objects.get_answers(question)

    return render_to_response('question.html', {
        'tittle': tittle,
        'answer_list' : answer_list,
        'question': question,
    })


def login(request):
    tittle = 'login'

    return render_to_response('login.html', {
        'tittle': tittle,
    })


def signup(request):
    tittle = 'signup'

    return render_to_response('signup.html', {
        'tittle': tittle,
    })


def ask(request):
    tittle = 'ask'

    return render_to_response('ask.html', {
        'tittle': tittle,
    })
