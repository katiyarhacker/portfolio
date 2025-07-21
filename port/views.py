from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return HttpResponse(request,'port/portfolio.html')