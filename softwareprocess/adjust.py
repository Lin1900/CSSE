import math
import re

def Adjust(values):
    if 'height' in values:
#        if values['height'].isalpha():
#            values['error'] = 'height is invalid'
#            return values
        # check there is only numbers in height
        if not isNumber(values['height']):
#        if not values['height'].isdigit():
            values['error'] = 'height is invalid'
            return values
        height = float(values['height'])
        if height < 0:
            values['error'] = 'height is invalid'
            return values
    else:
        height = 0

    if 'temperature' in values:
        #temp = int(values['temperature'])
        # check the temperature is in a valid range
        if not isNumber(values['temperature']):
            values['error'] = 'temperature is invalid'
            return values
        temp = int(values['temperature'])
        if temp < -20 or temp > 120:
            values['error'] = 'temperature is invalid'
            return values
    else:
        temp = 72

    if 'pressure' in values:
        pres = int(values['pressure'])
        # check the pressure is in a valid range
        if not isNumber(values['pressure']):
            values['error'] = 'pressure is invalid'
            return values
        if pres < 100 or pres > 1100:
             values['error'] = 'pressure is invalid'
             return values
    else:
        pres = 1010

    if 'horizon' in values:
        horizon = values['horizon']
        if horizon != 'artificial' and horizon != 'natural':
            values['error'] = 'horizon is invalid'
            return values
    else:
        horizon = 'natural'

    if 'alttitude' in values:
        values['error'] = 'altitude already exists'
        return values

    if 'observation' not in values:
        values['error'] = 'mandatory information is missing'
        return values

    degreeAndminute = values['observation'].split('d')
    degree = int(degreeAndminute[0])
    minute = float(degreeAndminute[1])

    if degree < 0 or degree >= 90:
        values['error'] = 'observation is invalid'
        return values

    if minute < 0.0 or minute >= 60.0:
        values['error'] = 'observation is invalid'
        return values

    # observation can't less than 0d0.1
    if degree == 0 and minute <= 0.1:
        values['error'] = 'observation is invalid'
        return values

    totalDegree = degree + (minute / 60.0)

    if horizon == 'natural':
        dip = (-0.97 * math.sqrt(height)) / 60.0
    else:
        dip = 0

    refraction = (-0.00452 * pres) / (273 + convert_to_celsius(temp)) / math.tan(math.radians(totalDegree))
    altitude = totalDegree + dip + refraction

    # convert altitude
    alMin = round((altitude - math.floor(altitude)) * 60.0, 1)
    alDeg = math.floor(altitude)
    newAl = '%d'%(alDeg) + 'd' + '%.1f'%(alMin)
    values['altitude'] = newAl
    return values

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def convert_to_celsius(i):
    return (i - 32) * 5.0/9.0
