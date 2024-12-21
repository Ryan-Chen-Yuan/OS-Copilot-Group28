from dateutil import parser


def parse_string_to_datetime_objects(input_str: str) -> tuple:
    """
    Parse the input string to extract datetime objects for the start time and end time.

    Args:
        input_str (str): A string that contains start and end times in various formats
                         (e.g., 'Dec 11 WED 6:30 pm - 8:30 pm' or 'November 28, 2024 4:00-5:30pm').

    Returns:
        tuple: A tuple containing two datetime objects, the first representing the start time,
               and the second representing the end time.
    """

    # Normalize the input string to handle different formats
    input_str = input_str.replace(" - ", " to ")

    # Split the input string into start and end parts
    if "to" in input_str:
        start_str, end_str = input_str.split(" to ")
    else:
        raise ValueError(
            "Input string must contain a 'to' separator for start and end times."
        )

    # Parse start and end time strings using dateutil.parser
    start_datetime = parser.parse(start_str.strip())
    end_datetime = parser.parse(end_str.strip())

    # Return the datetime objects
    return start_datetime, end_datetime
