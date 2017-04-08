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
        if len(date)

def checkDate(dates):
    if len(dates) != 3:
        return -1
