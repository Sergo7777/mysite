from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.core import serializers
from django.conf import settings
from django import forms

import datetime
from django.core.urlresolvers import reverse

from .forms import OrderForm, CommentForm

from .models import Order, Table, Stock, CategoryMenu, Food, Comment
import datetime
# Create your views here.
def home(request):
    return render(request, 'bar/index.html', )

def menu(request):
    category = CategoryMenu.objects.get(id=1)
    foods = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=2)
    foods2 = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=3)
    foods3 = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=4)
    foods4 = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=5)
    foods5 = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=6)
    foods6 = Food.objects.filter(category=category)
    category = CategoryMenu.objects.get(id=7)
    foods7 = Food.objects.filter(category=category)
    categories = CategoryMenu.objects.all()
    return render(request, 'bar/menu.html', {'foods': foods, 'foods2': foods2,
                                     'foods3': foods3,'foods4': foods4,'foods5': foods5,'foods6': foods6, 'foods7': foods7, 'categories':categories})

def table_list(request):
    form = OrderForm()
    tables = Table.objects.all()
    return render(request, 'bar/table_list.html', {'form': form, 'tables':tables, })

def information(request):
    return render(request, 'bar/information.html', )

def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'bar/shares.html', {'stocks': stocks})

def date_input(request):
    date = request.POST.get('date')
    ordered_table = serializers.serialize('json', 
                        Order.objects.filter(date=date))
    return HttpResponse(ordered_table, )


def send_mail(request): 
    tables = Table.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)     
        if form.is_valid():
            subject = ('Заказ стола в D.O.M')
            order = form.save(commit=False)
            date = form.cleaned_data['date']
            print(date)
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            table = form.cleaned_data['table']
            message = 'Вы заказали стол № {} на дату {}.  На Ваш е-mail отправлено сообщение о бронировании столика. Ждем Вас в нашем ресторане.'.format(table.id, date)
            if subject and email and message:
                try:
                    mail = EmailMessage(subject, message, 
                                settings.EMAIL_HOST_USER, [email],)
                    mail.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                order.save()
            date = date.strftime('%Y-%m-%d')
            form = OrderForm(initial={'date': date})
            return render(request, 'bar/table_list.html', {'form':form, 'tables': tables, 'message': message})
        else:
            message1 = 'Проверьте, пожалуйста, правильность заполнения данных.'
            form = OrderForm(request.POST)
        return render(request, 'bar/table_list.html', {'form':form, 'tables': tables, 'message1': message1})

def comments(request):
    comments = Comment.objects.all()
    five = Comment.objects.filter(comment_like=5)
    four = Comment.objects.filter(comment_like=4)
    three = Comment.objects.filter(comment_like=3)
    two = Comment.objects.filter(comment_like=2)
    one = Comment.objects.filter(comment_like=1)
    form = CommentForm()
    paginator = Paginator(comments, 3) 

    page = request.GET.get('page')
    try:
        comments= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)

    return render(request, 'bar/comments.html', {'comments': comments, 'form': form, 'five': five, 
                                                'one': one, 'two':two, 'three': three, 'four': four})

def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            comment.save()
            form.save()
            return redirect('comments')
    else:
        form = CommentForm()
    return render(request, 'bar/comments.html', {'form': form})

    
