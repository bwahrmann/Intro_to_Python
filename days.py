def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            return 28
        else:
            return 30
    return 30


def nextDay(year, month, day):
    """assumes all months have 30 days """
    if day < daysInMonth(year, month):
            return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year +1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """returns true if year1 month1 and day1 is before 
     year2, month2 and day 2, Assumes inputs are valid dates 
     in gregorian Calendar"""

    days = 0
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


print daysInMonth(2013,1)
print daysBetweenDates(2013, 1, 1, 2013, 1, 1)
print daysBetweenDates(2013, 1, 1, 2013, 1, 2)


def test():
    # tests with 30-day months!
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == ( 2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2012, 2, 28) == (2013, 3, 1)
    assert nextDay(2012, 9, 30) == (2013, 10, 1)
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    print "Tests finished!"
