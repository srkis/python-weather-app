# 🌤️ Python Weather App

A simple and modern web application built with **Python and Flask** that displays current weather, an hourly forecast for today, and a 5-day weather forecast for any city.

The app uses the **WeatherAPI** service to fetch real-time and forecast weather data and dynamically updates the UI based on weather conditions.

---

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Current temperature and “feels like” temperature
- 💨 Wind speed, humidity, and air pressure
- 🌅 Sunrise and sunset times
- 🕒 Hourly forecast for the current day
- 📅 5-day weather forecast
- 🎨 Dynamic backgrounds based on weather conditions
- ❗ User-friendly error handling when a city is not found

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Jinja2**
- **HTML / CSS**
- **WeatherAPI** – https://www.weatherapi.com/

---

## 📡 Weather API

This project uses **WeatherAPI** to retrieve weather data.

Example endpoint:

`https://api.weatherapi.com/v1/forecast.json`

Supported data:
- Current weather conditions
- Hourly forecast
- Multi-day forecast
- Local time and timezone data

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/srkis/python-weather-app.git
cd python-weather-app
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

You need a WeatherAPI key. Get a free key at: https://www.weatherapi.com/

Recommended (environment variable):

```bash
export WEATHERAPI_KEY="YOUR_WEATHERAPI_KEY"
```

Alternatively, you can add the key directly in the file that makes the API request (for example `server.py` or `weather.py`). It's recommended to use an environment variable to avoid committing secrets.

Example (in Python):

```python
import os
API_KEY = os.getenv('WEATHERAPI_KEY', 'YOUR_WEATHERAPI_KEY')
```

### 5. Run the application

```bash
python server.py
```

The app will be available at:

`http://localhost:5000`

---

## ☁️ Deployment

- The project's GitHub repository is connected to Render.com for automatic deployment.
- The application is live at: `https://python-app-weather-z0ad.onrender.com/`
- When you push to the connected GitHub branch, Render will automatically build and deploy the latest changes.
- Recommended: keep sensitive keys (like `API_KEY`) out of the repo and set them as environment variables in your Render service settings.


## ❗ Error Handling

- If the entered city is not found, the app displays a clear error message.
- If the city input is empty, the user is prompted to enter a valid city name.

---

## 📸 UI Overview

- Weather cards for daily forecasts
- Hourly forecast section for the current day
- Automatic background changes based on weather conditions (sunny, cloudy, rainy, night, snow)

---

## 📌 Future Improvements

- 🌍 Automatic user location detection
- ⭐ Favorite cities feature
- 📱 Improved mobile responsiveness
- 🌐 Multi-language support

---

## 📄 License

This project is open-source and available for personal and educational use.

---

## 👤 Author

Srđan Stojanović
GitHub: https://github.com/srkis
