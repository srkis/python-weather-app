from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from datetime import datetime

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/weather")
def get_weather():
    city = request.args.get('city')

    # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'Belgrade'

    weather_data = get_current_weather(city)

    #city is not found by API

    if 'error' in weather_data:
        error_code = weather_data['error'].get('code')

        if error_code == 1006:
            msg = "City not found. Check that you entered the name correctly."
        else:
            msg = "An error occurred while fetching the weather forecast."

        return render_template(
            "weather.html",
            error_message=msg
        )

    condition_text = weather_data['current']['condition']['text'].lower()
    is_day = weather_data['current']['is_day']  # 1 = dan, 0 = noć
    today_hours = weather_data['forecast']['forecastday'][0]['hour']

    if is_day == 0:
        weather_bg = "night-bg"
    elif "sun" in condition_text or "clear" in condition_text:
        weather_bg = "sunny-bg"
    elif "cloud" in condition_text or "overcast" in condition_text:
        weather_bg = "cloudy-bg"
    elif "rain" in condition_text or "drizzle" in condition_text:
        weather_bg = "rainy-bg"
    elif "storm" in condition_text or "thunder" in condition_text:
        weather_bg = "stormy-bg"
    elif "snow" in condition_text or "sleet" in condition_text:
        weather_bg = "snow-bg"
    else:
        weather_bg = "cloudy-bg"  # fallback

    forecast_days = weather_data['forecast']['forecastday'][:5]
    forecast = []

    hourly_forecast = []

    for hour in today_hours:
        hourly_forecast.append({
            "time": hour['time'].split(" ")[1][:5], #uzima se samo HH:MM
            "temp": round(hour['temp_c']),
            "icon": hour['condition']['icon'],
            "text": hour['condition']['text']
        })

    for day in forecast_days:
        date_obj = datetime.strptime(day['date'], "%Y-%m-%d")

        forecast.append({
            "day_name": date_obj.strftime("%A"),  # Monday, Tuesday...
            "max": round(day['day']['maxtemp_c']),
            "min": round(day['day']['mintemp_c']),
            "text": day['day']['condition']['text'],
            "icon": day['day']['condition']['icon'],
            "bg": get_bg_class(day['day']['condition']['text'])
        })


    return render_template(
        "weather.html",
        weather_data = weather_data,
        title=weather_data['location']['name'],
        temp=f"{weather_data['current']['temp_c']:.0f}",
        feels_like=f"{weather_data['current']['feelslike_c']:.0f}",
        condition=f"{weather_data['current']['condition']['text']}",
        condition_icon=f"{weather_data['current']['condition']['icon']}",
        wind_speed=f"{weather_data['current']['wind_kph']:.0f}",
        humidity=f"{weather_data['current']['humidity']:.0f}",
        pressure=f"{weather_data['current']['pressure_mb']:.0f}",
        sunset = f"{weather_data['forecast']['forecastday'][0]['astro']['sunset']}",
        sunrise = f"{weather_data['forecast']['forecastday'][0]['astro']['sunrise']}",
        weather_bg=weather_bg,
        forecast=forecast,
        hourly_forecast=hourly_forecast

    )

def get_bg_class(condition_text, is_day=1):
    text = condition_text.lower()
    if "sun" in text or "clear" in text:
        return "sunny-bg"
    elif "cloud" in text or "overcast" in text:
        return "cloudy-bg"
    elif "rain" in text:
        return "rainy-bg"
    elif "storm" in text or "thunder" in text:
        return "stormy-bg"
    elif "snow" in text:
        return "snow-bg"
    return "cloudy-bg"

if __name__ == "__main__":
    serve(app,host="0.0.0.0", port=5000)