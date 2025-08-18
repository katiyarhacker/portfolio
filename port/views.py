from django.shortcuts import render
from django.http import HttpResponse
import requests

def portfolio(request):
    return render(request, 'port/portfolio1.html')

# Google site verification
def google6cb7990a59be90b8(request):
    return HttpResponse(
        "google-site-verification: google6cb7990a59be90b8.html",
        content_type="text/html"
    )

def weatherapp(request):
    city = request.GET.get('q')
    weather_data = None

    # Default background
    default_background = "https://tse4.mm.bing.net/th/id/OIP.GsImz-edoeuqCMfKxDus0wHaEo?pid=Api&P=0&h=180"

    if city:
        api_key = "6d176ca2486c2b6d39802be973d6f2a8"  # Apni API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            condition = data['weather'][0]['main'].lower()

            # Weather condition ke hisaab se background select
            if "cloud" in condition:
                background_image = "https://images.unsplash.com/photo-1499346030926-9a72daac6c63"
            elif "rain" in condition:
                background_image = "https://images.unsplash.com/photo-1501594907352-04cda38ebc29"
            elif "clear" in condition:
                background_image = "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
            elif "snow" in condition:
                background_image = "https://images.unsplash.com/photo-1608889172617-6ec78dcf19cc"
            elif "mist" in condition or "fog" in condition:
                background_image = "https://images.unsplash.com/photo-1505483531331-fc3cf89fd382"
            else:
                background_image = default_background

            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'].title(),
                'background_image': background_image
            }

    return render(request, 'port/weatherapp.html', {
        'weather_data': weather_data,
        'default_background': default_background
    })
