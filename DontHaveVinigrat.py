import datetime
import random
from xmlrpc.client import Boolean


def random_date():
    first_date = input("Enter first date in format YYYY-MM-DD: ")
    second_date = input("Enter second date in format YYYY-MM-DD: ")
    try:
        first_date = datetime.date.fromisoformat(first_date)
        second_date = datetime.date.fromisoformat(second_date)
    except ValueError as e:
        print(f"{e.args} Date is not as the format described")
        return

    if check_if_date_on_day(0, first_date, second_date):
        print("I dont have any vinigrat")


def check_if_date_on_day(day, first_date, second_date) -> Boolean:
    """
    :param day: The day to check
    :param first_date: First date input.
    :param second_date: Second date input.
    :return: Boolean that indicate if the random date is on the chosen day.
    """
    time_delta = abs(first_date - second_date)
    if first_date > second_date:
        random_date_for_vini = first_date + datetime.timedelta(days=random.randrange(time_delta.days))
    else:
        random_date_for_vini = second_date + datetime.timedelta(days=random.randrange(time_delta.days))
    return random_date_for_vini.weekday() == day


if __name__ == '__main__':
    random_date()
