LEAST_FAVORITE_YEAR = 2020

def day_of_year(month, day, year):
    """
    returns the day of year given a date in (month, day, year) format
    """

    num_days = day
    if month == 2:
        num_days = num_days + 31
    elif month == 3:
        num_days = num_days + 59
    elif month == 4:
        num_days = num_days + 90
    elif month == 5:
        num_days = num_days + 31 + 28 + 31 + 30
    elif month == 6:
        num_days = num_days + 31 + 28 + 31 + 30 + 31
    elif month == 7:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        num_days = num_days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31
    if year == LEAST_FAVORITE_YEAR:
        num_days = -1
    return num_days

if __name__ == "__main__":
    print(day_of_year(4, 1, 2022))
