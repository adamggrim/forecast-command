import argparse

import requests
from bs4 import BeautifulSoup, Tag

from ._constants import HelpMessages
from ._exceptions import HTMLElementNotFoundError


def parse_args() -> str | None:
    """
    Parse command-line arguments for a temperature scale.

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
    Extract the forecast from the HTML for a given URL.

    Args:
        url: The URL to access for weather data.

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
