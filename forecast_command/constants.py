class HelpMessages:
    """
    Help message strings for command-line arguments.

    Attributes:
        DESCRIPTION: Description for temperature scale arguments.

        CELSIUS: Help message for -c/--celsius argument.
        FAHRENHEIT: Help message for -f/--fahrenheit argument.
    """
    DESCRIPTION: str = 'Make an optional specification for temperature scale.'

    CELSIUS: str = 'get the forecast in Celsius'
    FAHRENHEIT: str = 'get the forecast in Fahrenheit'

# Prompt for the user for another zip code.
ANY_OTHER_ZIP_PROMPT: str = 'Any other zip code? (5 digits):'

# Inputs for selecting Celsius.
CELSIUS_INPUTS: set[str] = {'celsius', 'c'}

# Suffix appended to a URL for Celsius forecasts.
CELSIUS_URL_SUFFIX: str = '&FcstType=text&unit=1'

# Name for the directory containing data files.
DATA_DIR_NAME: str = 'data'

# Prompt for the user to enter a temperature scale.
ENTER_TEMP_SCALE_PROMPT: str = (
    'Enter a temperature scale (Celsius [C] or Fahrenheit [F]):'
)

# Prompt for when the previous temperature scale input was invalid.
ENTER_VALID_TEMP_SCALE_PROMPT: str = (
    'Please enter Celsius (C) or Fahrenheit (F):'
)

# Prompt for when the previous zip code input was invalid.
ENTER_VALID_ZIP_PROMPT: str = 'Please enter a valid zip code:'

# Prompt for the user to enter a zip code.
ENTER_ZIP_PROMPT: str = 'Enter zip code (5 digits):'

# Inputs for exiting the program.
EXIT_INPUTS: set[str] = {'quit', 'q', 'exit', 'e'}

# Message for when the user exits the program.
EXIT_MESSAGE: str = 'Exiting the program...'

# Inputs for selecting Fahrenheit.
FAHRENHEIT_INPUTS: set[str] = {'fahrenheit', 'f'}

# Prefix for when the HTML element for the forecast is not found.
HTML_ELEMENT_NOT_FOUND_MESSAGE: str = (
    'HTML element not found: '
)

# Inputs for indicating a negative response.
NO_INPUTS: set[str] = {'no', 'n'}

# Message for when there is no internet connection.
NO_INTERNET_CONNECTION_MESSAGE: str = (
    'No internet connection. Please try again.'
)

# Message for when the request times out.
REQUEST_TIMEOUT_MESSAGE: str = 'The request timed out. Please try again.'

# Prefix for unexpected errors.
UNEXPECTED_ERROR_MESSAGE: str = 'An unexpected error occurred: '

# Inputs for indicating an affirmative response.
YES_INPUTS: set[str] = {'yes', 'y'}

# The file name of the zip code to URL map.
ZIP_CODE_TO_URL_MAP_FILE_NAME: str = 'zip_code_to_url_map.json'
