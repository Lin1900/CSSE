import math
import StarsTable

def Predict(values):

    starName = values['body'][0].upper() + values['body'][1:].lower()
    if starName not in StarsTable.stars:
        values['error'] = 'star not in catalog'
        return values
    #star = StarsTable.getStarData(starName).split(',')

    if 'body' not in values:
        values['error'] = 'Mandatory information is missing'
        return values
    if 'lat' in values:
        values['error'] = 'Latitude is invalid'
        return values
    if 'long' in values:
        values['error'] = 'Longitude is invalid'
        return values

    if 'date' not in values:
        values['date'] = '2001-01-01'
    else:
        date = values['date'].split('-')
        if len(date) != 3:
            values['error'] = 'date is invalid'
            return values
        if checkDate(date) == -1:
            values['error'] = 'date is invalid'
            return values



def checkDate(dates):
    year = dates[0]    #check year
    if not year.isdigit() or len(year) != 4:
        return -1
    if int(year) < 2001:
        return -1
    month = dates[1]   #check month
    if not month.isdigit() or len(month) != 2:
        return -1
    if int(month) <= 0 or int(month) > 12:
        return -1
    day = dates[2]     #check day
    if not day.isdigit() or len(day) != 2:
        return -1
    day = int(day)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day != 31:
           return -1
    if month == 2 and year % 4 == 0:     #check leap year
        if day != 29:
            return -1
    if month == 02 and year % 4 == 0:
        if day != 28:
            return -1
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day != 30:
            return -1
