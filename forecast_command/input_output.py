import os
import textwrap

import requests

from forecast_command.config import zip_code_url_dict
from forecast_command.constants import (
    ANY_OTHER_ZIP_PROMPT,
    CELSIUS_URL_SUFFIX,
    ENTER_VALID_TEMP_SCALE_PROMPT,
    ENTER_VALID_ZIP_PROMPT,
    ENTER_ZIP_PROMPT,
    EXIT_MESSAGE,
    NO_INPUTS,
    EXIT_INPUTS,
    YES_INPUTS
)
from forecast_command.enums import TempScale
from forecast_command.parsing import (
    format_forecasts,
    parse_forecast
)
from forecast_command.exceptions import (
    HTMLElementNotFoundError,
    InvalidTempScaleError,
    InvalidUrlFormatError,
    InvalidZipCodeFormatError,
    NoDataForZipCodeError,
    NoTempScaleError,
    NoZipCodeError,
    ZipCodeNotFoundError
)
from forecast_command.validation import (
    validate_temp_scale,
    validate_url,
    validate_zip_code
)


class ForecastLoop:
    """A controller to manage the weather forecast prompt loop."""

    def __init__(self):
        """
        Initialize a new ForecastLoop instance by prompting the user to
        enter a zip code.
        """
        print_wrapped(ENTER_ZIP_PROMPT)

    def fahrenheit(self) -> None:
        """Run the input loop for printing forecasts in Fahrenheit."""
        self._process_zip_input(TempScale.FAHRENHEIT)

    def celsius(self) -> None:
        """Run the input loop for printing forecasts in Celsius."""
        self._process_zip_input(TempScale.CELSIUS)

    def _process_zip_input(self, temp_scale: TempScale) -> None:
        """
        Prompt the user to enter a zip code, print the forecast for
        that zip code and prompt the user to enter any other zip code.

        Args:
            temp_scale (TempScale): The temperature scale for the
                forecast.
        """
        # While loop to deploy functions and get input from the user
        while True:
            url: str | None = self._retrieve_url_from_zip(temp_scale)
            if url is None:
                break
            self._print_forecast(url)
            print_wrapped(ANY_OTHER_ZIP_PROMPT)

    def _retrieve_url_from_zip(self, temp_scale: TempScale) -> str | None:
        """
        Request a valid zip code that matches a zip code in the JSON file
        and return the matching URL.

        Args:
            temp_scale: The temperature scale to apply to the forecast.

        Returns:
            url: The URL for the zip code input.
            None: If the user signals to exit.
        """
        while True:
            zip_code_input: str = input().strip().lower()

            if zip_code_input in (NO_INPUTS | EXIT_INPUTS):
                return None
            elif zip_code_input in YES_INPUTS:
                print_wrapped(ENTER_VALID_ZIP_PROMPT)
                continue

            try:
                validate_zip_code(zip_code_input)
                url = zip_code_url_dict[zip_code_input]
                if temp_scale == TempScale.CELSIUS:
                    url += CELSIUS_URL_SUFFIX
                validate_url(url)
                return url
            except (
                NoZipCodeError,
                InvalidZipCodeFormatError
            ) as e:
                print_wrapped(str(e))
                print_wrapped(ENTER_VALID_ZIP_PROMPT)
            except (
                ZipCodeNotFoundError,
                NoDataForZipCodeError,
                InvalidUrlFormatError
            ) as e:
                print_wrapped(str(e))
                print_wrapped(ANY_OTHER_ZIP_PROMPT)

    def _print_forecast(self, url: str) -> None:
        """
        Print forecast data from a given URL to the console.

        Args:
            url: The URL for accessing weather data.
        """
        try:
            day_forecasts: list[str] = parse_forecast(url)
            formatted_forecasts: list[str] = format_forecasts(day_forecasts)
            for day_forecast in formatted_forecasts:
                print_wrapped(day_forecast)
        except requests.exceptions.ConnectionError:
            print_wrapped('No internet connection. Please try again.')
        except requests.exceptions.Timeout:
            print_wrapped('The request timed out. Please try again.')
        except HTMLElementNotFoundError as e:
            print_wrapped(f'HTML element not found: {e}')
        except Exception as e:
            print_wrapped(f'An unexpected error occurred: {e}')


def print_padding() -> None:
    """Print a blank line for padding."""
    print('')


def print_wrapped(text: str) -> None:
    """
    Wrap printing based on the width of the terminal and begin the
    string with a newline character.

    Args:
        text: The string to print.
    """
    terminal_size: int = os.get_terminal_size()[0]
    print_size: int = terminal_size - 1
    wrapped_text: str = textwrap.fill(text, width=print_size)
    print('\n' + wrapped_text)


def program_exit() -> None:
    """Print a message that the program is exiting, then exit the
    program."""
    print_wrapped(EXIT_MESSAGE)
    print_padding()
    exit()


def prompt_for_temp_scale() -> str | None:
    """
    Prompt the user for a valid temperature scale.

    Returns:
        str: A string representing Fahrenheit or Celsius.
        None: If the user signals to exit.
    """
    while True:
        temp_scale_input: str = input().strip().lower()
        if temp_scale_input in (NO_INPUTS | EXIT_INPUTS):
            return None
        else:
            try:
                validate_temp_scale(temp_scale_input)
            except (NoTempScaleError, InvalidTempScaleError) as e:
                print_wrapped(str(e))
                print_wrapped(ENTER_VALID_TEMP_SCALE_PROMPT)
            else:
                return temp_scale_input
