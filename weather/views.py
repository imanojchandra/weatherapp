# from django.shortcuts import render
# import requests
# import datetime

# def index(request):
#     weather_data = None
#     error_message = None
#     city_local_time = None

#     if request.method == 'POST':
#         city = request.POST.get('city')

#         # OpenWeatherMap API URL (replace with your API key)
#         api_key = 'a71f14b4302749e54df5704454c7c4d1'
#         weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

#         response = requests.get(weather_url)

#         if response.status_code == 200:
#             weather_data = response.json()

#             # Calculate local time for the city
#             timezone_offset = weather_data['timezone']
#             city_local_time = datetime.datetime.utcfromtimestamp(
#                 weather_data['dt'] + timezone_offset
#             ).strftime('%d-%m-%Y, %I:%M %p')
#         else:
#             error_message = 'City not found'

#     return render(request, 'weather/index.html', {
#         'weather_data': weather_data,
#         'error_message': error_message,
#         'city_local_time': city_local_time
#     })



from django.shortcuts import render, redirect
import requests
import datetime

def index(request):
    weather_data = None
    error_message = None
    city_local_time = None

    if request.method == 'POST':
        city = request.POST.get('city')

        # OpenWeatherMap API URL
        api_key = 'a71f14b4302749e54df5704454c7c4d1'
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(weather_url)

        if response.status_code == 200:
            weather_data = response.json()

            # local time for the city
            timezone_offset = weather_data['timezone']
            city_local_time = datetime.datetime.utcfromtimestamp(
                weather_data['dt'] + timezone_offset
            ).strftime('%d-%m-%Y, %I:%M %p')  

            # Store the weather data in the session
            request.session['weather_data'] = weather_data
            request.session['city_local_time'] = city_local_time

            return redirect('index')

        else:
            error_message = 'City not found'

    # Handle GET request or page refresh, i.e. show data if it exists
    weather_data = request.session.get('weather_data')
    city_local_time = request.session.get('city_local_time')

    # Clear the session on refresh
    if request.method == 'GET':
        request.session.pop('weather_data', None)
        request.session.pop('city_local_time', None)

    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error_message': error_message,
        'city_local_time': city_local_time
    })
