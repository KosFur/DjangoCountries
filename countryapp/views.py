from django.shortcuts import render
import string
from django.core.paginator import Paginator

def welcome_page(request):
    return render(request, 'countryapp/welcome_page.html')


def countries_list(request):
    countries = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) >= 3:
                name = elements[1]
                countries.append(name)
    
    print(countries)  
    return render(request, 'countryapp/countries_list.html', {'countries': countries})

def country_detail(request, country_name):
    languages = []
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) == 4:
                code, name, capital, langs = elements
                if name == country_name:
                    languages = langs.split(';')
                    break
            elif len(elements) == 3:
                code, name, capital = elements
                if name == country_name:
                    languages = ["Language data not available"]
                    break
    
    return render(request, 'countryapp/country_detail.html', {'country_name': country_name, 'languages': languages})

def languages_list(request):
    languages = set()
    
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) == 4:
                code, name, capital, langs = elements
                langs_list = langs.split(';')
                languages.update(langs_list)

    return render(request, 'countryapp/languages_list.html', {'languages': sorted(languages)})

def language_detail(request, language):
    countries = []
    
    with open('countries.txt', 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            if len(elements) == 4:
                code, name, capital, langs = elements
                if language in langs.split(';'):
                    countries.append(name)

    return render(request, 'countryapp/countries_by_language.html', {'language': language, 'countries': countries})