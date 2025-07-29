# Forecast Command

`forecast-command` is a Python package for retrieving forecasts from NOAA (National Oceanic and Atmospheric Administration) and printing them to the console. For a given zip code, `forecast-command` can print a seven-day forecast in Fahrenheit or Celsius.

## Requirements

- Python 3.9

## Dependencies

`forecast-command` requires the following Python libraries:

- `beautifulsoup4`: For parsing HTML data retrieved from weather.gov
- `requests`: For making HTTP requests to retrieve forecast data from weather.gov

## Example

This example demonstrates how to retrieve a weather forecast using `forecast-command`.

1. **Run the command**

    Once `forecast-command` is installed, call `forecast` from the command line.

    For a forecast in Celsius, you can also call `forecast -c`. For a forecast in Fahrenheit, you can call `forecast -f`.

2. **Enter a temperature scale**

    If you did not already indicate a temperature scale, the program will prompt you for one:

    ```
    Enter a temperature scale (Celsius [C] or Fahrenheit [F]):
    Celsius
    ```

3. **Enter a zip code**

    The program will then prompt you to enter a zip code:

    ```
    Enter zip code (5 digits):
    80204
    ```

4. **Print the forecast**

    The program will print a seven-day weather forecast in reverse chronological order, so that the current day appears closest to the bottom of the output:

    ```
    Sunday: A chance of rain. Partly sunny, with a high near 12.

    Saturday Night: A chance of rain. Mostly cloudy, with a low around 6.

    Saturday: Mostly sunny, with a high near 20.

    Friday Night: Partly cloudy, with a low around 1.

    Friday: A chance of rain before noon. Partly sunny, with a high near 15.

    Thursday Night: A chance of snow. Mostly cloudy, with a low around 2.

    Thursday: A chance of snow. Partly cloudy, with a high near 13.

    Wednesday Night: Mostly cloudy, with a low around 10.

    Wednesday: Mostly sunny, with a high near 22.

    Tuesday Night: Mostly cloudy, with a low around 5.

    Tuesday: Sunny, with a high near 18.

    Monday Night: Mostly clear, with a low around 1.

    Monday: Sunny, with a high near 20.

    Overnight: Mostly clear, with a low around 3.
    ```

5. **Continue or exit**

    The program will prompt you for another zip code. To exit, type `no` (`n`), `quit` (`q`) or `exit` (`e`), or trigger a KeyboardInterrupt (Ctrl + C):

    ```
    Any other zip code?:
    ^C

    Exiting the program...
    ```

## Structure

```
forecast_command/
└── data/
|   └── zip_code_to_url_map.json: Maps zip code strings to weather.gov forecast URL strings
├── __init__.py: File for recognizing the package
├── __main__.py: Runs the forecast command
├── config.py: Loads JSON file for use in the package
├── constants.py: Defines constants used throughout the package
├── enums.py: Defines enum for temperature scales
├── exceptions.py: Defines custom exceptions for data and input errors
├── input_output.py: Handles user input and console output
├── parsing.py: Parses input, HTML data and command-line arguments
├── regexes.py: Defines regular expressions for parsing
└── validation.py: Defines functions for validating input
```

## Usage

Follow these steps to run `forecast-command`:

1. **Install Python**: Verify that you have Python 3.9 or later. You can install Python at `https://www.python.org/downloads/`.

You can check your Python version with the `python --version` command (`python3 --version` on macOS/Linux).

2. **Install the package**: Install `forecast-command` using pip.

    On Windows:

    ```
    pip install git+https://github.com/adamggrim/forecast-command.git
    ```

    On macOS/Linux:

    ```
    pip3 install git+https://github.com/adamggrim/forecast-command.git
    ```

4. **Run the program**: Execute the program by calling `forecast`, `forecast -c` (for Celsius) or `forecast -f` (for Fahrenheit) from the command line.

## Troubleshooting (macOS/Linux)

If the console cannot find the `forecast` command when you try to run it from the command line, it was not installed on your system's PATH.

To resolve this, follow these steps:

1. Find the installed location of the `forecast-command` package using pip's `show` command.

    On Windows:
    ```
    pip3 show forecast-command
    ```

    On macOS/Linux:
    ```
    pip3 show forecast-command
    ```

    The location of `forecast-command` will be listed in the command's output. For example:
    ```
    Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
    ```

2. Once you have determined the location of `forecast-command`, find the installed location of the `forecast` command file in your parent Python folder.

    On macOS:
    ```
    find /Library/Frameworks/Python.framework/Versions/3.12/ -name forecast
    ```

    On Linux:
    ```
    find /home/user/.local/ -name forecast
    ```

3. Create a symbolic link to the underlying `forecast` command file and place it in the local directory on your system's PATH.

    On macOS:

    ```
    sudo ln -s /Library/Frameworks/Python.framework/Versions/3.12/bin/forecast /usr/local/bin/
    ```

    On Linux:

    ```
    sudo ln -s /home/user/.local/bin/forecast /usr/local/bin/
    ```

    To find the system's PATH, you can type `echo $PATH` into the console (macOS/Linux).

## License

This project is licensed under the MIT License.

## Contributors

- Adam Grim (@adamggrim)
