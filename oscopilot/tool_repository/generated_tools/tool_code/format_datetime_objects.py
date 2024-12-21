from datetime import datetime


def format_datetime_objects(start_datetime: datetime, end_datetime: datetime) -> tuple:
    """
    Convert the given start and end datetime objects into the desired string formats
    using Python's datetime formatting features.

    Args:
        start_datetime (datetime): The starting datetime object.
        end_datetime (datetime): The ending datetime object.

    Returns:
        tuple: A tuple containing the formatted start and end datetime strings.
               Format example: ('2024年12月11日 18:30:00', '2024年12月11日 20:30:00')
    """
    # Define the format for converting the datetime object to the desired string format
    desired_format = "%Y年%m月%d日 %H:%M:%S"

    formatted_start = start_datetime.strftime(desired_format)

    formatted_end = end_datetime.strftime(desired_format)

    return formatted_start, formatted_end
