import math
import re

def Correct(values):
    if not ('lat' in values or 'long' in values or 'altitude' in values or 'assumedLat' in values or 'assumendLong' in values):
        values['error'] = 'Mandatory information is missing'
        return values

    if ('correctedDistance' in values or 'correctedAzimuth' in values):
        values['error'] = 'correctedDistance or correctedAzimuth is invalid'
        return values

    #if ('correctedDistance' in values):
    #     values['error'] = 'correctedDistance or correctedAzimuth is invalid'
    #     return values
    #if ('correctedAzimuth' in values):
    #     values['error'] = 'correctedDistance or correctedAzimuth is invalid'
    #     return values

    assumedLat = values['assumedLat']    #check type
    if not isinstance(assumedLat,str):
       values['error'] = 'input is invalid'
       return values
    if 'd' not in assumedLat:
        values['error'] = 'assumedLat is invalid'
        return values

    assumedLong = values['assumedLong']
    if not isinstance(assumedLong,str):
       values['error'] = 'input is invalid'
       return values
    if 'd' not in assumedLong:
        values['error'] = 'assumedLong is invalid'
        return values

    lat = values['lat']
    if not isinstance(lat,str):
       values['error'] = 'input is invalid'
       return values
    #if 'd' not in lat:
    #    values['error'] = 'lat is invalid'
    #    return values

    long = values['long']
    if not isinstance(long,str):
       values['error'] = 'input is invalid'
       return values
    if 'd' not in long:
        values['error'] = 'long is invalid'
        return values

    altitude = values['altitude']
    if not isinstance(altitude,str):
       values['error'] = 'input is invalid'
       return values
    if 'd' not in altitude:
        values['error'] = 'assumedLong is invalid'
        return values

    newassumedLong = values['assumedLong'].split('d')
    newassumedLat = values['assumedLat'].split('d')
    newlat = lat.split('d')
    newlong = long.split('d')

    if (int(newassumedLat[0]) >= 90 or int(newassumedLat[0]) <= -90):
        values['error'] = 'assumedLat is invalid'
        return values
    if (float(newassumedLat[1]) >= 60.0 or float(newassumedLat[1]) < 0.0):
        values['error'] = 'assumedLat is invalid'
        return values
    if not isNumber(newassumedLat[0] or newassumedLat[1]):
        values['error'] = 'assumedLat is invalid'
        return values
    if (int(newassumedLong[0]) >= 360 or int(newassumedLong[0]) < 0):
        values['error'] = 'assumedLong is invalid'
        return values
    if (float(newassumedLong[1]) >= 60.0 or float(newassumedLat[1]) < 0.0):
        values['error'] = 'assumedLat is invalid'
        return values
    if not isNumber(newassumedLong[0] or newassumedLong[1]):
            values['error'] = 'assumedLong is invalid'
            return values

    LHA = degreeToMinute(long) + degreeToMinute(assumedLong)
    intermediateDistance = (math.sin(math.radians(degreeToMinute(lat))) * math.sin(math.radians(degreeToMinute(assumedLat)))) + (math.cos(math.radians(degreeToMinute(lat))) * math.cos(math.radians(degreeToMinute(assumedLat))) * math.cos(math.radians(LHA)))
    correctedAltitude = math.degrees(math.asin(intermediateDistance))   #something wrong
    correctedDistance = degreeToMinute(altitude) - correctedAltitude
    values['correctedDistance'] = str(minutes_to_arc_minutes(minuteToDegree(correctedDistance)))

    Azimuth1 = math.sin(math.radians(degreeToMinute(lat))) - (math.sin(math.radians(degreeToMinute(assumedLat))) * intermediateDistance)
    Azimuth2 = math.cos(math.radians(degreeToMinute(assumedLat))) * math.cos(math.asin(intermediateDistance))
    correctedAzimuth = math.acos(Azimuth1 / Azimuth2)
    correctedAzimuth = math.degrees(correctedAzimuth)
    values['correctedAzimuth'] = minuteToDegree(correctedAzimuth)
    return values


def degreeToMinute(minutes):
    deg = float(minutes[0:minutes.find('d')])
    m = float(minutes[minutes.find('d')+1: len(minutes)])
    m = m / 60
    if minutes[0] == '-':
        deg = deg - m
    else:
        deg = deg + m

    # deg = deg + m
    # if minutes[0] == '-':
    #     deg = deg * (-1)
    return deg

def minuteToDegree(degrees):
    deg = int(degrees)
    degrees = abs(degrees - deg) * 60
    deg_string = str(degrees)
    if not(deg_string[deg_string.find('.')+2: deg_string.find('.')+3] == ''):
        if (int(deg_string[deg_string.find('.')+2: deg_string.find('.')+3]) > 4):
            degrees = degrees + 0.1

    deg_minutes = str(degrees)[0:str(degrees).find('.')+2]
    while deg > 360:
        deg = deg - 360

    if float(deg_minutes) < 10.0:
        altitude = str(deg) + 'd0' + deg_minutes
    else:
        altitude = str(deg) + 'd' + deg_minutes
    return altitude

def minutes_to_arc_minutes(deg):
    degDegrees = deg[0: deg.find('d')]
    degMinutes = deg[deg.find('d')+1: len(deg)]
    degArcMinutes = int(degDegrees) * 60 + int(float(degMinutes))

    return degArcMinutes

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


"""
def degreeToMinute(n):
    degree = n.split('d')
    deg = degree[0]
    newDeg = int(deg)
    minute = float(degree[1])
    if newDeg != 0:
        if deg[0] < 0:
            degree = newDeg - minute / 60
        else:
            degree = newDeg + minute / 60
    else:
        if deg[0] == '-':
            degree = - minute / 60
        else:
            degree = minute / 60
    return degree

def minuteToDegree(degree):
    minute = str("{:.1f}".format((degree - int(degree)) * 60))
    if '-' in minute:
        minute = minute.replace('-', '')
    minute = minute.split('.')
    min1 = minute[0].zfill(2)
    min2 = minute[1]
    minute = min1 + '.' + min2
    degree = int(degree) - 360
    degree = str(degree) + 'd' + minute
    return degree

def minutes_to_arc_minutes(deg):
    degDegrees = deg[0: deg.find('d')]
    degMinutes = deg[deg.find('d')+1: len(deg)]
    degArcMinutes = int(degDegrees) * 60 + int(float(degMinutes))
    return degArcMinutes

"""
