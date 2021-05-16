from django.shortcuts import render


def county_search(request):
    return render(request, 'county_search/county_search.html')
