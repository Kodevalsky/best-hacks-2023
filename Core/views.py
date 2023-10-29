from django.shortcuts import render
from .forms import AnnouncementForm
from Offer.models import Announcement, AnnouncementImages, Review, Comment
from User.forms import RegisterForm, LoginForm
from User.models import User

def index(request):
    register = RegisterForm()
    login = LoginForm()
    PromotedOffers = Announcement.objects.filter(promoted=True)
    images = []
    for offer in PromotedOffers:
        image = AnnouncementImages.objects.filter(announcement_id=offer.id).first()
        images.append(image)
    zip_list = zip(PromotedOffers, images)
    form = AnnouncementForm()
    context = {
        'offers': zip_list,
        'regform' : register,
        'logform' : login,
        'form'  : form
    }
    if request.method == 'GET':
        context['offers'] = zip_list
    elif request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            location = form.cleaned_data.get("location")
            announcements = Announcement.objects.filter(
                title__startswith = title,
                location__startswith = location
            )
            context['offers'] = zip(announcements, images)
            context['form'] = form
        else:
            context['form'] = form
    else:
        pass
    return render(request, 'Core/index.html', context)

def register(request):
    if request.method == 'POST':
        registerdata = RegisterForm(request.POST)
        if registerdata.is_valid():
            registerobj = registerdata.save(commit=False)
            registerobj.set_password(registerobj.password)
            registerobj.save()
            return render(request, 'Core/index.html', context)
        else:
            print(registerdata.errors.as_data())
            return render(request, 'Core/index.html', {'form': register})
    else:
        return render(request, 'Core/index.html', {'form': register})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'Core/index.html', context)
    else:
        return render(request, 'Core/index.html', {})

def about_us(request):
    return render(request, 'Core/about_us.html', {})

def offers(request):
    return render(request, 'offers.html', {})

def single_offer(request):
    return render(request, 'single_offer.html', {})

def your_visits(request):
    return render(request, 'your_visits.html', {})

def single_visit(request):
    return render(request, 'single_visit.html', {})
