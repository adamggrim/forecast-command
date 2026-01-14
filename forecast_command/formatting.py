from ._regexes import ParsingRegexes


def format_forecasts(forecasts_text: list[str]) -> list[str]:
    """
    Format the forecast list elements for printing.

    Args:
        forecasts_text: A list of strings representing days and their
            forecasts, beginning with the soonest forecast.

    Returns:
        forecasts_text: A list of reformatted strings.
    """
    for i, forecast_text in enumerate(forecasts_text):
        # Remove extra spaces.
        forecast_text: str = ParsingRegexes.DUPLICATE_SPACES.sub(
            '', forecast_text
        )
        # Add a space before a.m. and p.m.
        forecast_text = ParsingRegexes.AM_PM_BOUNDARY.sub(' ', forecast_text)
        # Standardize the format of a.m. and p.m.
        forecast_text = ParsingRegexes.AM_PM_FORMAT.sub('.m.', forecast_text)
        forecasts_text[i] = forecast_text
    return forecasts_text
