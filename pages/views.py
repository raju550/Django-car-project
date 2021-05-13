from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_features=True)
    all_car=Car.objects.order_by('-created_date')
    # search_field=Car.objects.values('model','state','year','body_style')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_car': featured_car,
        'all_car':all_car,
        # 'search_field':search_field,
        'model_search':model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
