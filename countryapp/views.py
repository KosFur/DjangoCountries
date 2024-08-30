from django.shortcuts import render
import string
from django.core.paginator import Paginator
from collections import defaultdict


def welcome_page(request):
    return render(request, 'countryapp/welcome_page.html')


def countries_list(request, letter=None):
    countries = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) == 4:
                code, name, capital, languages = elements
            elif len(elements) == 3:
                code, name, capital = elements
            if letter is None or name.startswith(letter):
                countries.append(name)

    paginator = Paginator(countries, 10)  # 10 стран на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'countryapp/countries_list.html', {'page_obj': page_obj, 'letter': letter})

def country_detail(request, country_name):
    languages = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) >= 3:
                name = elements[1]
                if name == country_name:
                    langs = elements[3].split(';')
                    languages = langs if langs else ["Язык не указан"]
                    break
    
    return render(request, 'countryapp/country_detail.html', {'country_name': country_name, 'languages': languages})

def languages_list(request):
    languages = defaultdict(list)
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) >= 4:
                country = elements[1]
                langs = elements[3].split(';')
                for lang in langs:
                    languages[lang.strip()].append(country)
    
    return render(request, 'countryapp/languages_list.html', {'languages': dict(languages)})

def language_detail(request, language_name):
    countries = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) >= 4:
                langs = elements[3].split(';')
                if language_name in langs:
                    countries.append(elements[1])
    
    return render(request, 'countryapp/language_detail.html', {'language_name': language_name, 'countries': countries})

def countries_by_letter(request, letter):
    countries = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) >= 3:
                _, name, _ = elements[:3]
                if name.startswith(letter):
                    countries.append(name)
    return render(request, 'countryapp/countries_list.html', {'countries': countries, 'letter': letter})
