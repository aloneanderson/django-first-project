from django.shortcuts import render

# Create your views here.
import random
from django.http import HttpResponse
from django.shortcuts import render


def first(request):
    return render(request, 'first.html')


def article_1(request):
    return render(request, 'second.html')


def article_2(request):
    return render(request, 'third.html')


def user_article(request):
    return HttpResponse('by aloneanderson')


def article_number(request, article_id, slug_text=''):
        return render(request, 'article.html', {'article_id': article_id, 'slug_text': slug_text})



def users_number_article(request, article_id):
    return HttpResponse(f'User number id is: {article_id}')


def phone(request, phone_number):
    return HttpResponse(f'Phone number is: {phone_number}')


def mark(request, mark_text):
    return HttpResponse(f'Symbols is: {mark_text}')


def index(request):
    return render(request, 'index.html', {'random_id': random.randint(1, 100)})


def main_page(request):
    return render(request, 'base.html')


def random_int(request):
    return render(request, 'random.html', {
        'random_int': random.randrange(1, 100),
    })
