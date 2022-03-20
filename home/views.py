from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('<h1>Hello, Mihai</h1>')


def show_details_students(request):

    details_students = {
        'all_students':[
            {
                'first_name':'George',
                'last_name':'Popescu',
                'age':30,
                'is_olympic':False
            },
            {
                'first_name':'Miclea',
                'last_name':'Andrei',
                'age':35,
                'is_olympic':True
            },
            {
                'first_name':'Ionescu',
                'last_name':'Andreea',
                'age':20,
                'is_olympic':False

            }
        ]
    }

    return render(request, 'home/details_students.html', details_students)


def show_details_cars(request):
    details_cars = {
        'all_cars': [
            {
                'car_brand': 'Volkswagen',
                'car_model': 'Touran 1',
                'year': 2005,
                'number_of_km': 180000,
                'horse_power':110,
                'is_new':False
            },
            {
                'car_brand': 'Audi',
                'car_model': 'RS7',
                'year': 2022,
                'number_of_km':0,
                'horse_power': 520,
                'is_new': True
            },
            {
                'car_brand': 'Dacia',
                'car_model': 'Golan 2',
                'year': 2007,
                'number_of_km': 320000,
                'horse_power': 79,
                'is_new': False
            },
            {
                'car_brand':'Porsche',
                'car_model':'Panamera',
                'year':2015,
                'number_of_km':250000,
                'horse_power':320,
                'is_new':False
            }

        ]
    }

    return render(request, 'home/details_cars.html', details_cars)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
