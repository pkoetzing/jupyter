def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

is_leap(1900), is_leap(1950), is_leap(2000)