from forecast_command.constants import (
    CELSIUS_INPUTS,
    ENTER_TEMP_SCALE_PROMPT,
    FAHRENHEIT_INPUTS
)
from forecast_command.input_output import (
    ForecastLoop,
    print_padding,
    print_wrapped,
    program_exit,
    prompt_for_temp_scale
)
from forecast_command.parsing import parse_args


def main() -> None:
    """
    Initiates an instance of ForecastLoop and optionally prompts the
        user to run the program in Fahrenheit or Celsius.
    """
    temp_scale_input: str | None = parse_args()

    if temp_scale_input is None:
        print_wrapped(ENTER_TEMP_SCALE_PROMPT)

    while True:
        try:
            if temp_scale_input is None:
                temp_scale_input = prompt_for_temp_scale()
            forecast_loop: ForecastLoop = ForecastLoop()
            if temp_scale_input in CELSIUS_INPUTS:
                forecast_loop.celsius()
            elif temp_scale_input in FAHRENHEIT_INPUTS:
                forecast_loop.fahrenheit()
        except KeyboardInterrupt:
            print_padding()
            program_exit()
