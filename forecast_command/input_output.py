import os
import textwrap

import requests

from forecast_command.config import zip_codes_dict
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

    def _process_zip_input(self, temp_scale: TempScale) -> None:
        """
        Prompt the user to enter a zip code, print the forecast for
        that zip code, and prompt the user to enter any other zip
        code.

        Args:
            temp_scale (TempScale): The temperature scale for the
                forecast.
        """
        # While loop to deploy functions and get input from the user
        while True:
            url: str = retrieve_url_from_zip(temp_scale)
            print_forecast(url)
            print_wrapped(ANY_OTHER_ZIP_PROMPT)

    def fahrenheit(self) -> None:
        """
        Run the input loop for printing forecasts in Fahrenheit.

        Args:
            self: The instance of the ForecastLoop class.
        """
        self._process_zip_input(TempScale.FAHRENHEIT)

    def celsius(self) -> None:
        """
        Run the input loop for printing forecasts in Celsius.

        Args:
            self: The instance of the ForecastLoop class.
        """
        self._process_zip_input(TempScale.CELSIUS)


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


def prompt_for_temp_scale() -> str:
    """
    Prompt the user for a valid temperature scale.

    Returns:
        str: A string representing Fahrenheit or Celsius.
    """
    while True:
        temp_scale_input: str = input().strip().lower()
        if temp_scale_input in (NO_INPUTS | EXIT_INPUTS):
            program_exit()
        else:
            try:
                validate_temp_scale(temp_scale_input)
            except (NoTempScaleError, InvalidTempScaleError) as e:
                print_wrapped(str(e))
                print_wrapped(ENTER_VALID_TEMP_SCALE_PROMPT)
            else:
                return temp_scale_input


def retrieve_url_from_zip(temp_scale: TempScale) -> str:
    """
    Request a valid zip code that matches a zip code in the JSON file
    and return the matching URL.

    Args:
        temp_scale: The temperature scale to apply to the forecast.

    Returns:
        url: The url for the zip code input.
    """
    def handle_zip_code_error(e: Exception, prompt: str) -> None:
        """
        Handle exceptions related to ZIP code processing, printing an
        error message and prompt.

        Args:
            e: The raised exception.
            prompt: The prompt to print.
        """
        print_wrapped(str(e))
        print_wrapped(prompt)
    while True:
        zip_code_input: str = input().strip().lower()
        if zip_code_input in (NO_INPUTS | EXIT_INPUTS):
            program_exit()
        elif zip_code_input in YES_INPUTS:
            print_wrapped(ENTER_VALID_ZIP_PROMPT)
        else:
            try:
                validate_zip_code(zip_code_input)
                if temp_scale == TempScale.CELSIUS:
                    url: str = zip_codes_dict[zip_code_input] + CELSIUS_URL_SUFFIX
                else:
                    url: str = zip_codes_dict[zip_code_input]
                validate_url(url)
            except (
                NoZipCodeError,
                InvalidZipCodeFormatError
            ) as e:
                handle_zip_code_error(str(e), ENTER_VALID_ZIP_PROMPT)
            except (
                ZipCodeNotFoundError,
                NoDataForZipCodeError,
                InvalidUrlFormatError
            ) as e:
                handle_zip_code_error(str(e), ANY_OTHER_ZIP_PROMPT)
            else:
                return url


def print_forecast(url: str) -> None:
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
