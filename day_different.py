def day_difference(day1: int, day2: int) -> int:
    """ Return the number of days between 
    day1 and day2, which are both in the
    range 1-365 (thu indicating the day of the year
    >>> day_difference(200, 224)
    24
    >>> day_difference(50, 50)
    0
    >>> day_difference(100, 99)
    -1
    """
    return day2 - day1


print(day_difference(200, 224))
print(day_difference(50, 50))
print(day_difference(100, 99))


# Designing Three Birthday-Related Functions
