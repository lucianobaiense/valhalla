#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from dashboard.models import Profile, News, Reader, System, Change

#---------------------------------------------------------
#    Functions
#---------------------------------------------------------

def system_notify(message, link, request):
    system_notify = System(
        message = message,
        link = link,
        reader = User.objects.get(username=request.user.username),
    )
    system_notify.save()
    return

#---------------------------------------------------------
#    Views
#---------------------------------------------------------

def health(request):
    if request.method == 'GET':
        return HttpResponse('OK', status=200)
    else:
        return HttpResponse('Method Not Allowed', status=405)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/', status=200)
    else:
        return render(request, 'dashboard/landings/login.html')

def login_authenticate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                request.user.profile
                return redirect('/home/', status=200)
            except:
                return redirect('/register/', status=200)
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponse('Method Not Allowed', status=405)

def logout_account(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/', status=200)
    else:
        return HttpResponse('Method Not Allowed', status=405)

@login_required(login_url='/')
def register(request):
    username_id = request.user.id
    profile = Profile.objects.filter(username_id=username_id)
    if profile:
        return redirect('/home/', status=200)
    else:
        return render(request, 'dashboard/landings/register.html')

@login_required(login_url='/')
def create_profile(request):
    if request.method == 'POST':
        profile_create = Profile(
            username = User.objects.get(username=request.user.username),
            photo = request.FILES['photo'],
            nickname = request.POST['nickname'],
            telegram = request.POST['telegram'],
            skype = request.POST['skype'],
            hipchat = request.POST['hipchat'],
            phone = request.POST['phone'],
            about = request.POST['about'],
            agent = True,
        )
        profile_create.save()
        system_notify("Bem vindo a Valhalla!","/about", request)
        return redirect('/home', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required(login_url='/')
def home(request):
    return render(request, 'dashboard/landings/home.html')

@login_required(login_url='/')
def dashboard(request):
    context = {
        'section': "Dashboard",
        'section_icon': "dashboard",
    }
    return render(request, 'dashboard/sections/dashboard.html', context)

@login_required(login_url='/')
def leaderboard(request):
    context = {
        'section': "Leaderboard",
        'section_icon': "trending_up",
    }
    return render(request, 'dashboard/sections/leaderboard.html', context)

@login_required(login_url='/')
def news(request):
    reader_id = request.user.id
    news = News.objects.exclude(Q(author_id=reader_id) | Q(readers=reader_id)).values().order_by('-created')
    history = News.objects.filter(Q(author_id=reader_id) | Q(readers=reader_id)).values().order_by('-created')

    news_photo = False
    history_photo = False

    for n in news:
        username = User.objects.get(id=n['author_id'])
        n['username'] = username
        try:
            profile = Profile.objects.filter(username=username).values_list('photo', flat=True)[0]
            n['photo'] = profile
            news_photo = True
        except:
            news_photo = False

    for h in history:
        username = User.objects.get(id=h['author_id'])
        h['username'] = username
        try:
            profile = Profile.objects.filter(username=username).values_list('photo', flat=True)[0]
            h['photo'] = profile
            history_photo = True
        except:
            history_photo = False

    context = {
        'section': "Notícias",
        'section_icon': "rss_feed",
        'reader_id' : reader_id,
        'news' : news,
        'history' : history,
        'news_photo' : news_photo,
        'history_photo' : history_photo
    }
    return render(request, 'dashboard/sections/news.html', context)

@login_required(login_url='/')
def create_news(request):
    if request.method == 'POST':
        news_create = News(
            author = User.objects.get(username=request.user.username),
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        news_create.save()
        return redirect('/news', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required(login_url='/')
def update_news(request):
    if request.method == 'POST':
        return redirect('/news', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required(login_url='/')
def delete_news(request):
    if request.method == 'POST':
        news = News.objects.get(id=request.POST['news_id'])
        news.delete()
        return redirect('/news', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)


@login_required(login_url='/')
def read(request):
    if request.method == 'GET':
        notification_id = request.GET['id']
        url = request.GET['redirect']
        System.objects.filter(id=notification_id).update(
            read=True,
        )
        return redirect(url, status=200)
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required(login_url='/')
def indicators(request):
    context = {
        'section': "Indicadores",
        'section_icon': "insert_chart",
    }
    return render(request, 'dashboard/sections/indicators.html', context)

@login_required(login_url='/')
def changes(request):
    changes_list = Change.objects.all()
    paginator = Paginator(changes_list, 20)
    page = request.GET.get('page')
    changes = paginator.get_page(page)
    context = {
        'section': "Mudanças",
        'section_icon': "date_range",
        'changes' : changes,
    }
    return render(request, 'dashboard/sections/changes.html', context)

@login_required(login_url='/')
def profile(request):
    profile = Profile.objects.filter(username_id=request.user.id).values()
    name = request.user.first_name + " " + request.user.last_name
    context = {
        'section': "Profile",
        'section_icon': "face",
        'profile' : profile,
        'name' : name
    }
    return render(request, 'dashboard/sections/profile.html', context)

@login_required(login_url='/')
def profile_update(request):
    if request.method == 'POST':
        user_id = request.user.id
        profile_update = Profile.objects.get(username=user_id)
        profile_update.photo = request.FILES['photo']
        profile_update.nickname = request.POST['nickname']
        profile_update.telegram = request.POST['telegram']
        profile_update.hipchat = request.POST['hipchat']
        profile_update.skype = request.POST['skype']
        profile_update.phone = request.POST['phone']
        profile_update.about = request.POST['about']
        profile_update.save()
        return redirect('/profile', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required(login_url='/')
def about(request):
    context = {
        'section': "Sobre",
        'section_icon': "library_books",
    }
    return render(request, 'dashboard/sections/about.html', context)
