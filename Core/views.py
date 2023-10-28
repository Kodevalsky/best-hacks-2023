from django.shortcuts import render
from .forms import AnnouncementForm

def index(request):
    #data = User.objects.all()
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            location = form.cleaned_data.get("location")
            announcements = AnnouncementForm.objects.filter(
                title__startwith = title,
                location__startwith = location
            )
            context = {"form":form, "announcements":announcements}
        else:
            context = {"form":form}
    else:
        form = AnnouncementForm()
        context = {"form":form}
    return render(request, 'Core/index.html', context)

def register(request):
    return render(request, 'register.html', {})

def login(request):
    return render(request, 'login.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})

def offers(request):
    return render(request, 'offers.html', {})

def single_offer(request):
    return render(request, 'single_offer.html', {})

def your_visits(request):
    return render(request, 'your_visits.html', {})

def single_visit(request):
    return render(request, 'single_visit.html', {})
