import holidays
from datetime import date, timedelta

def calculate_base_price(number_of_days, price_of_single_room, number_of_room):
    return float(number_of_days * price_of_single_room * number_of_room)

def count_holidays_in_range(start_date, end_date, country_code='US'):
    """Counts the number of public holidays within the given date range.

    Args:
        start_date: The start date of the range (datetime.date object).
        end_date: The end date of the range (datetime.date object).
        country_code: The country code for holidays (default is 'US').

    Returns:
        The number of public holidays within the range.
    """
    country_holidays = holidays.CountryHoliday('SG')
    holiday_count = 0
    for ordinal_date in range(start_date.toordinal(), end_date.toordinal() + 1):
        date_obj = date.fromordinal(ordinal_date)
        if date_obj in country_holidays:
            holiday_count += 1  # Increment count if date is a holiday
    return holiday_count

