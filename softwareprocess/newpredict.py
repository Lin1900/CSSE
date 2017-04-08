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
        #check 'year' valid or not
        year = date[0]
        if int(year) < 2001:
            values['error'] = 'date is invalid'
            return values
        if not year.isdigit() or len(year) != 4:
            values['error'] = 'date is invalid'
            return values
        year = int(year)
        #check 'month' valid or not
        month = date[1]
        if len(month) != 2:
            values['error'] = 'date is invalid'
            return values
        if not month.isdigit() or int(month) > 12 or int(month) < 0:
            values['error'] = 'date is invalid'
            return values
        month = int(month)
        #check 'day' valid or not
        day = (date[2])
        if not day.isdigit() or len(day) != 2:
            values['error'] = 'date is invalid'
            return values
        day = int(day)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day != 31:
                values['error'] = 'date is invalid'
                return values
        if month == 2 and year % 4 == 0:     #check leap year
            if day != 29:
                values['error'] = 'date is invalid'
                return values
        if month == 02 and year % 4 != 0:
            if day != 28:
                values['error'] = 'date is invalid'
                return values
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day != 30:
                values['error'] = 'date is invalid'
                return values

    if 'time' not in values:
        values['time'] = '00:00:00'
    else:
        time = values['time'].split(':')
        if len(time) != 3:
            values['error'] = 'time is invalid'
            return values
        # check hour valid or not
        hour = time[0]
        if not hour.isdigit() or len(hour) != 2:
            values['error'] = 'time is invalid'
            return values
        hour = int(hour)
        if hour >= 24 or hour < 0:
            values['error'] = 'time is invalid'
            return values
        # check minutes valid or not
        minute = time[1]
        if not minute.isdigit() or len(minute) != 2:
            values['error'] = 'time is invalid'
            return values
        minute = int(minute)
        if minute >= 60 or minute < 0:
            values['error'] = 'time is invalid'
            return values
        # check second valid or not
        second = time[2]
        if not second.isdigit() or len(second) != 2:
            values['error'] = 'time is invalid'
            return values
        second = int(second)
        if second >= 60 or second < 0:
            values['error'] = 'time is invalid'
            return values
