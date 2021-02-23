import json
from urllib import request, error

from styles import Style


class NoConfigError(Exception):
    pass


def retrieve_data(location):
    """
    Calls upon the OpenWeatherMap API to retrieve weather information for a given place.

    :param location: The location where the weather information is wished to be queried from.
    :return:
    """
    api_key = ""

    try:
        # noinspection SpellCheckingInspection
        with request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)) as url:
            data = json.load(url)
            return data
    except error.HTTPError as httpError:
        print(
            "{}An error occurred; a {}{} response code{}{} was given. Please try again.{}".format(Style.RED, Style.BOLD,
                                                                                                  httpError.code,
                                                                                                  Style.END, Style.RED,
                                                                                                  Style.END))
