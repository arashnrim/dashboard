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
    # WARNING: This API key is public here only for the reason of making development easier. Since this is an
    # educational project and not a commercial one, I think that it is acceptable not to safeguard the API key.
    # If this were an actual commercial project for everyone to see, the API key should be guarded.
    api_key = "a7f952efb5473d28dab30ba75920daa3"

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
