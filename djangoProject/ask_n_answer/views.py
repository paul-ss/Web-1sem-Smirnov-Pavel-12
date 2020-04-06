# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response  #optional

from django.http import HttpResponse, HttpResponseNotFound
import random
from django.core.urlresolvers import reverse
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from djangoProject.settings import PER_PAGE, N_POPULAR_TAGS, N_POPULAR_USERS


from ask_n_answer.models import *





def get_right_bar():
    right_bar = dict.fromkeys(['tags', 'users'])
    right_bar['tags'] = Tag.objects.get_popular(N_POPULAR_TAGS)

    right_bar['users'] = Profile.objects.get_popular(N_POPULAR_USERS)
    #['User ' + str(random.randint(0,10)) for i in range(5)]
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




def not_found(request):
    return HttpResponseNotFound('<h1>404 Page not found</h1>')




def index(request):
    tittle = "index"

    question_list = Question.objects.new_questions()
    question_list_current_page, page = paginate(question_list, request)

    return render_to_response('index.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })




def hot(request):
    tittle = 'hot'

    question_list = Question.objects.hot_questions()
    question_list_current_page, page = paginate(question_list, request)

    return render_to_response('hot.html', {
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })



def tag(request, tag = None):
    tittle = "tag: " + tag

    question_list = Question.objects.tag_questions(tag)
    question_list_current_page, page = paginate(question_list, request)

    return render_to_response('tag.html', {
        'tag' : tag,
        'tittle': tittle,
        'question_box_list': question_list_current_page,
        'page': page,
        'right_bar': get_right_bar(),
    })



def question(request, id = None):
    tittle = "question: " + id

    question = Question.objects.pk_question(id)
    if question == None:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')

    answer_list = Answer.objects.get_answers(question)

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
