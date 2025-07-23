from django.shortcuts import render
from django.http import HttpResponse

def portfolio(request):
    return render(request, 'port/portfolio.html')

# Google site verification
def google6cb7990a59be90b8(request):
    return HttpResponse("google-site-verification: google6cb7990a59be90b8.html", content_type="text/html")
