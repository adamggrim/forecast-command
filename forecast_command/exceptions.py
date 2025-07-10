class HTMLElementNotFoundError(Exception):
    """Exception raised when a given HTML element cannot be found."""


class InvalidTempScaleError(Exception):
    """Exception raised when the provided temperature scale string is
    invalid."""


class InvalidUrlFormatError(Exception):
    """Exception raised when the provided string does not match
    weather.gov's forecast URL syntax."""


class InvalidZipCodeFormatError(Exception):
    """Exception raised when the provided string is not a valid zip
    code."""


class NoTempScaleError(Exception):
    """Exception raised when the provided temperature scale string is
    empty."""


class NoDataForZipCodeError(Exception):
    """Exception raised when there is no data available for the given
    zip code."""


class NoZipCodeError(Exception):
    """Exception raised when the provided string is empty."""


class ZipCodeNotFoundError(Exception):
    """Exception raised when the zip code string is not found in the
    given JSON file."""
