import datetime
import random


def random_date():
    first_date = input("Enter first date in format YYYY-MM-DD: ")
    second_date = input("Enter second date in format YYYY-MM-DD: ")
    try:
        first_date = datetime.date.fromisoformat(first_date)
        second_date = datetime.date.fromisoformat(second_date)
    except ValueError:
        print("date is not as the format described")
        return
    if first_date > second_date:
        Timedelta = first_date - second_date
    else:
        Timedelta = second_date - first_date

    random_date_for_vini = datetime.date

    if first_date > second_date:
        random_date_for_vini = first_date + datetime.timedelta(days=random.randrange(Timedelta.days))
    else:
        random_date_for_vini = second_date + datetime.timedelta(days=random.randrange(Timedelta.days))

    if random_date_for_vini.weekday() == 0:
        print("I dont have any vinigrat")


random_date()
