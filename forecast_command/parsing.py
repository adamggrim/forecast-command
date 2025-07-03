import argparse
import re

import requests
from bs4 import BeautifulSoup, Tag

from forecast_command.constants import HelpMessages
from forecast_command.regexes import ParsingRegexes
from forecast_command.validation import HTMLElementNotFoundError


def parse_args() -> str | None:
    """
    Parses command-line arguments for a temperature scale.

    Returns:
        str | None: A string representing a specified temperature 
            scale, otherwise None.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=HelpMessages.DESCRIPTION
    )
    group: argparse._MutuallyExclusiveGroup = (
        parser.add_mutually_exclusive_group()
    )
    group.add_argument(
        '-c', 
        '--celsius', 
        action='store_true', 
        help=HelpMessages.CELSIUS
    )
    group.add_argument(
        '-f', 
        '--fahrenheit', 
        action='store_true', 
        help=HelpMessages.FAHRENHEIT
    )
    args: argparse.Namespace = parser.parse_args()
    if args.celsius:
        return 'celsius'
    elif args.fahrenheit:
        return 'fahrenheit'
    else:
        return None


def parse_forecast(url: str) -> list[str]:
    """
    Extracts the forecast from the HTML for a given URL.

    Args:
        url: The url to access for weather data.

    Returns:
        list[str]: A list of strings pairing each day string with a 
            forecast string.
    """
    nws_page: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(nws_page.content, 'html.parser')
    forecast_body: Tag | None = soup.find(
        'div', {'id': 'detailed-forecast-body'}
    )
    if forecast_body is None:
        raise HTMLElementNotFoundError(
            'Forecast body not found for that zip code.'
        )
    days: list[str] = [b.string for b in forecast_body.find_all('b')]
    if not days:
        raise HTMLElementNotFoundError(
            'Forecast days not found for that zip code.'
        )
    forecasts_text: list[str] = [
        forecast_text.get_text() 
        for forecast_text in soup.select('div[class *= "forecast-text"]')
    ]
    if not forecasts_text:
        raise HTMLElementNotFoundError(
            'Forecast text not found for that zip code.'
        )
    # Reverse the order of the strings so the current day appears closest to 
    # the console prompt in the output.
    return [
        day + ': ' + forecast_text 
        for day, forecast_text in zip(
            days[::-1], forecasts_text[::-1]
        )
    ]


def format_forecasts(forecasts_text: list[str]) -> list[str]:
    """
    Formats the forecast list elements for printing.

    Args:
        forecasts_text: A list of strings representing days and their 
            forecasts, beginning with the soonest forecast.

    Returns:
        forecasts_text: A list of reformatted strings.
    """
    for index, forecast_text in enumerate(forecasts_text):
        # Remove extra spaces.
        forecast_text: str = ParsingRegexes.DUPLICATE_SPACES.sub(
            '', forecast_text
        )
        # Add a space before a.m. and p.m.
        forecast_text = ParsingRegexes.AM_PM_BOUNDARY.sub(' ', forecast_text)
        # Standardize the format of a.m. and p.m.
        forecast_text = ParsingRegexes.AM_PM_FORMAT.sub('.m.', forecast_text)
        forecasts_text[index] = forecast_text
    return forecasts_text
