from .config import zip_code_to_url_map
from .constants import (
    CELSIUS_INPUTS,
    FAHRENHEIT_INPUTS
)
from .exceptions import (
    InvalidTempScaleError,
    InvalidUrlFormatError,
    InvalidZipCodeFormatError,
    NoDataForZipCodeError,
    NoTempScaleError,
    NoZipCodeError,
    ZipCodeNotFoundError
)
from .regexes import ValidationRegexes


def validate_temp_scale(temp_scale_input: str) -> None:
    """
    Validate a temperature scale string.

    This funciton checks whether the string is in the sets
    CELSIUS_INPUTS or FAHRENHEIT_INPUTS.

    Args:
        temp_scale_input: A string representing a temperature scale.

    Raises:
        NoTempScaleError: If the input string is empty.
        InvalidTempScaleError: If the input is not a valid scale.
    """
    if temp_scale_input == '':
        raise NoTempScaleError('No temperature scale entered.')
    elif (temp_scale_input not in CELSIUS_INPUTS and temp_scale_input not in
          FAHRENHEIT_INPUTS):
        raise InvalidTempScaleError('Not a valid temperature scale.')


def validate_zip_code(zip_code_input: str) -> None:
    """
    Validate a zip code string.

    This function checks whether the string consists of a sequence of
    five digits.

    Args:
        zip_code_input: A string representing a zip code.

    Raises:
        NoZipCodeError: If the input string is empty.
        InvalidZipCodeFormatError: If the input is not five digits.
        ZipCodeNotFoundError: If the zip code is not in the data source.
        NoDataForZipCodeError: If the zip code exists but has no data.
    """
    if zip_code_input == '':
        raise NoZipCodeError('No zip code entered.')
    elif not ValidationRegexes.ZIP_CODE.match(zip_code_input):
        raise InvalidZipCodeFormatError('Invalid zip code format.')
    elif zip_code_input not in zip_code_to_url_map:
        raise ZipCodeNotFoundError('Zip code not found.')
    elif zip_code_to_url_map[zip_code_input] == '':
        raise NoDataForZipCodeError(f'No data available for {zip_code_input}.')


def validate_url(url: str) -> None:
    """
    Validate a URL string.

    This function checks whether the string matches weather.gov's
    forecast URL syntax.

    Args:
        url: A string representing a URL.

    Raises:
        InvalidUrlFormatError: If the URL does not match the expected
            syntax.
    """
    if not ValidationRegexes.URL.match(url):
        raise InvalidUrlFormatError('Invalid URL for that zip code.')
