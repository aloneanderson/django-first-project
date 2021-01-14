from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def first(request):
    return HttpResponse("Here you can watch games")


def index(request):
    return HttpResponse("Hello, this is game site")


def article_1(request):
    return HttpResponse('Cyberpunk 2077')


def article_2(request):
    return HttpResponse('Metro Exodus')


def user_article(request):
    return HttpResponse('by aloneanderson')


def article_number(request, article_id, slug_text=''):
    return HttpResponse(
        f'Number of this article is: {article_id} and text: {slug_text}'
        if slug_text else f'Number of this article is: {article_id}')


def users_number_article(request, article_id):
    return HttpResponse(f'User number id is: {article_id}')


def phone(request, phone_number):
    return HttpResponse(f'Phone number is: {phone_number}')


def mark(request, mark_text):
    return HttpResponse(f'Symbols is: {mark_text}')
