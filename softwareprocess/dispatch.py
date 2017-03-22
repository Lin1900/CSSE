"""
    Created on March 19, 2017
    @author: Linyuan Zhang
"""

#import math
#import re

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values



    #Perform designated function
    if(values['op'] == 'adjust'):
        return Adjust(values)   #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values

    # adjusts the celestial sighting
def Adjust(values):
    if 'height' in values:
        height = float(values['height'])
        if height < 0:
            values['error'] = 'height is invalid'
            return values
    else:
        height = 0

    if 'temperature' in values:
        temp = int(values['temperature'])
        if temp < -20 or temp > 120:
            values['error'] = 'temperature is invalid'
            return values
    else:
        temp = 72

    if 'pressure' in values:
        pres = int(values['pressure'])
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
        values['error'] = 'missing observation'
        return values

    degreeAndminute = values['observation'].split('d')
    degree = int(degreeAndminute[0])
    minute = float(degreeAndminute[1])

    if degree < 0 or degree >= 90:
        values['error'] = 'degree is invalid'
        return values

    if minute < 0.0 or minute >= 60.0:
        values['error'] = 'minute is invalid'
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

    # conver altitude
    alMin = round((altitude - math.floor(altitude)) * 60.0, 1)
    alDeg = math.floor(altitude)
    newAl = '%d'%(alDeg) + 'd' + '%.1f'%(alMin)
    values['altitude'] = newAl
    return values

def convert_to_celsius(i):
    return (i - 32) * 5.0/9.0


