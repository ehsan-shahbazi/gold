from django.shortcuts import render
from .models import Material, News, User
from .forms import NewUserForm
from .tasks import *
from django.utils import timezone
from .tasks import wrap_all, wrap_news


# Create your views here.


def new_user(request):
    # if this is a POST request we need to process the form data
    context = {
        "materials": Material.objects.all()
    }
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name = form.data['name']
            email = form.data['email']
            user = User(name=name, email=email, last=timezone.now())
            user.save()
            # redirect to a new URL:
            return render(request, 'polls/index.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()
        # print('that was a get')
    return render(request, 'polls/index.html', context=context)


def make_money_string(money):
    money = str(money)
    if len(money) <= 6:
        money = money[:-3] + ',' + money[-3:]
    elif len(money) > 6:
        money = money[:-6] + ',' + money[-6:-3] + ',' + money[-3:]
    money = money.replace('1', '۱')
    money = money.replace('2', '۲')
    money = money.replace('3', '۳')
    money = money.replace('4', '۴')
    money = money.replace('5', '۵')
    money = money.replace('6', '۶')
    money = money.replace('7', '۷')
    money = money.replace('8', '۸')
    money = money.replace('9', '۹')
    money = money.replace('0', '۰')
    return money


def home(request):
    mats = Material.objects.all()
    # wrap_all()
    strings = []
    for mat in mats:
        strings.append([mat.persian_name, make_money_string(mat.sell_price), make_money_string(mat.buy_price)])
    context = {
        "materials": mats,
        "stringed": strings
    }
    return render(request, 'polls/index.html', context=context)


def tasks(request):
    wrap_news()
    wrap_all()
    context = {
        "materials": Material.objects.all()
    }
    return render(request, 'polls/index.html', context=context)



def contact(request):
    context = {
        "materials": Material.objects.all()
    }
    return render(request, 'polls/contact.html', context=context)


def make_user(request, email, name):
    # print(email)
    # print(name)
    # print(request)
    context = {
        "materials": Material.objects.all()
    }
    return render(request, 'polls/contact.html', context=context)


def news(request):
    all_news = News.objects.all()
    all_news = list(all_news)
    all_news.reverse()
    my_news = []
    first_news = []
    for i in range(min(int(len(all_news) / 3), 5)):
        if i != 0:
            my_news.append([all_news[3 * i], all_news[3 * i + 1], all_news[3 * i + 2]])
        else:
            first_news = [all_news[3 * i], all_news[3 * i + 1], all_news[3 * i + 2]]
    # print(my_news)
    context = {
        'first_news': first_news,
        'news': my_news
    }
    return render(request, 'polls/news.html', context=context)


def practice(request):
    context = {
        'content': 'hi there',
        'number': 2,
        'the_list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'num': int(timezone.now().time().microsecond)
    }
    return render(request, 'polls/first.html', context=context)
