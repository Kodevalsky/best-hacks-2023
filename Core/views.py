from django.shortcuts import render

def index(request):
    #data = User.objects.all()
    context = {"napis": "Witaj w Skillsprout!"}
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