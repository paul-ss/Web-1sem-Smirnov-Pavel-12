# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response  #optional

from django.http import HttpResponse
import random
from django.core.urlresolvers import reverse
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from djangoProject.settings import PER_PAGE



def get_right_bar():
    right_bar = dict.fromkeys(['tags', 'users'])
    right_bar['tags'] = ['tag' + str(random.randint(0,10)) for i in range(8)]
    right_bar['users'] = ['User ' + str(random.randint(0,10)) for i in range(5)]
    return right_bar


def paginate(objects_list, request):
    page_number = request.GET.get('page')
    if (page_number == None):
        page_number = 1

    paginator = Paginator(objects_list, PER_PAGE)
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

    question_box_list = []
    for i in range(17):
        question_box = dict.fromkeys(['question', 'description', 'rating', 'answers_count', 'tags', 'id'])
        question_box['id'] = random.randint(0,10)
        question_box['question'] = 'Question' + str(question_box['id'])
        question_box['description'] = 'Description' + str(question_box['id'])
        question_box['rating'] = random.randint(0,10)
        question_box['answers_count'] = str(random.randint(0,10))
        question_box['tags'] = ['tag' + str(random.randint(0,10)) for i in range(random.randint(1,4))]
        question_box_list.append(question_box)

        question_list_current_page, page = paginate(question_box_list, request)

    return render_to_response('index.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })




def hot(request):
    tittle = 'hot'
    question_box_list = []

    for i in range(23):
        question_box = dict.fromkeys(['question', 'description', 'rating', 'answers_count', 'tags', 'id'])
        question_box['id'] = random.randint(0,10)
        question_box['question'] = 'Question' + str(question_box['id'])
        question_box['description'] = 'Description' + str(question_box['id'])
        question_box['rating'] = random.randint(0,10)
        question_box['answers_count'] = str(random.randint(0,10))
        question_box['tags'] = ['tag' + str(random.randint(0,10)) for i in range(random.randint(1,4))]
        question_box_list.append(question_box)

        question_list_current_page, page = paginate(question_box_list, request)

    return render_to_response('hot.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })



def tag(request, tag = None):
    if tag == None:
        tittle = 'none'
    else :
        tittle = tag

    question_box_list = []

    for i in range(16):
        question_box = dict.fromkeys(['question', 'description', 'rating', 'answers_count', 'tags', 'id'])
        question_box['id'] = random.randint(0,10)
        question_box['question'] = 'Question' + str(question_box['id'])
        question_box['description'] = 'Description' + str(question_box['id'])
        question_box['rating'] = random.randint(0,10)
        question_box['answers_count'] = str(random.randint(0,10))
        question_box['tags'] = ['tag' + str(random.randint(0,10)) for i in range(random.randint(1,3))]
        question_box['tags'].append(tag)
        question_box_list.append(question_box)

        question_list_current_page, page = paginate(question_box_list, request)

    return render_to_response('tag.html', {
        'tag' : tag,
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })



def question(request, id = None):
    if id == None:
        tittle = 'none'
    else :
        tittle = 'question'

    question = dict.fromkeys(['question', 'description', 'rating', 'answers_count', 'tags', 'id'])
    question['question'] = 'Question' + str(id)
    question['description'] = 'Description' + str(id)
    question['rating'] = random.randint(0,10)
    question['answers_count'] = str(random.randint(0,10))
    question['tags'] = ['tag' + str(random.randint(0,10)) for i in range(random.randint(1,4))]
    question['id'] = id

    answer_list = []
    for i in range(5):
        answer = dict.fromkeys(['answer', 'rating', 'is_correct', 'image'])
        answer['answer'] = 'My answer for your question' + str(random.randint(0,10))
        answer['rating'] = random.randint(0,10)
        answer['is_correct'] = (i == 0)
        answer_list.append(answer)

    return render_to_response('question.html', {
        'tittle': tittle,
        'answer_list' : answer_list,
        'question': question,
        'right_bar': get_right_bar(),
    })


def login(request):
    tittle = 'login'

    return render_to_response('login.html', {
        'tittle': tittle,
        'right_bar': get_right_bar(),
    })


def signup(request):
    tittle = 'signup'

    return render_to_response('signup.html', {
        'tittle': tittle,
        'right_bar': get_right_bar(),
    })


def ask(request):
    tittle = 'ask'

    return render_to_response('ask.html', {
        'tittle': tittle,
        'right_bar': get_right_bar(),
    })
