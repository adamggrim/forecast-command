# --- Data Errors ---
class DataError(Exception):
    """Base class for data errors."""


class HTMLElementNotFoundError(DataError):
    """Exception raised when a given HTML element cannot be found."""


class NoDataForZipCodeError(DataError):
    """Exception raised when there is no data available for the given
    zip code."""


class ZipCodeNotFoundError(DataError):
    """Exception raised when the zip code string is not found in the
    given JSON file."""


# --- Input Errors ---
class InputError(Exception):
    """Base class for input errors."""


class InvalidTempScaleError(InputError):
    """Exception raised when the provided temperature scale string is
    invalid."""


class InvalidUrlFormatError(InputError):
    """Exception raised when the provided string does not match
    weather.gov's forecast URL syntax."""


class InvalidZipCodeFormatError(InputError):
    """Exception raised when the provided string is not a valid zip
    code."""


class NoTempScaleError(InputError):
    """Exception raised when the provided temperature scale string is
    empty."""


class NoZipCodeError(InputError):
    """Exception raised when the provided string is empty."""
