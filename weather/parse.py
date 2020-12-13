import weather.weatherart
from . import weatherart
from .styling import Style


def parse(data):
    temp = round(data["main"]["temp"] / 10, 2)
    condition = data["weather"][0]["description"].capitalize()
    feels_like = round(data["main"]["feels_like"] / 10, 2)
    wind_direction = data["wind"]["deg"]
    wind_speed = data["wind"]["speed"]
    if condition == "Clear sky":
        weatherart.clear_sky()
    elif condition == "Few clouds":
        weatherart.few_clouds()
    elif condition == "Scattered clouds":
        weatherart.scattered_clouds()
    elif condition == "Broken clouds":
        weatherart.broken_clouds()
    elif "rain" or "Rain" in condition:
        weatherart.rain()
    elif condition == "Thunderstorm":
        weatherart.thunderstorm()
    elif condition == "Snow":
        weatherart.snow()
    elif condition == "Mist":
        weatherart.mist()
    print("{}Current condition:{} {}".format(Style.YELLOW, Style.END, condition))
    print("{}Temperature:{} {}°C".format(Style.YELLOW, Style.END, temp))
    print("{}Feels like:{} {}°C".format(Style.YELLOW, Style.END, feels_like))
    wind_direction_arrow = ""
    if wind_direction == 0:
        wind_direction_arrow = "→"
    elif 0 < wind_direction < 90:
        wind_direction_arrow = "↗"
    elif wind_direction == 90:
        wind_direction_arrow = "↑"
    elif 90 < wind_direction < 180:
        wind_direction_arrow = "↖"
    elif wind_direction == 180:
        wind_direction_arrow = "←"
    elif 180 < wind_direction < 270:
        wind_direction_arrow = "↙"
    elif wind_direction == 270:
        wind_direction_arrow = "↓"
    elif 270 < wind_direction < 360:
        wind_direction_arrow = "↘"
    # noinspection PyUnboundLocalVariable
    print("{}Wind:{} {} {}m/s".format(Style.YELLOW, Style.END, wind_direction_arrow, wind_speed))
