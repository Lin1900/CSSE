import math


def Correct(values):
   # if ('lat' not in values or 'long' not in values or 'altitude' not in values or 'assumedLat' not in values or 'assumendLong' not in values):
    #    values['error'] = 'Mandatory information is missing'
     #   return values

    if ('correctedDistance' in values or 'correctedAzimuth' in values):
         values['error'] = 'correctedDistance or correctedAzimuth is invalid'
         return values

    assumedLat = values['assumedLat']
    if 'd' not in assumedLat:
        values['error'] = 'assumedLat is invalid'
        return values
    newassumedLat = values['assumedLat'].split('d')

    assumedLong = values['assumedLong']
    if 'd' not in assumedLong:
        values['error'] = 'assumedLong is invalid'
        return values
    newassumedLong = assumedLong = values['assumedLong'].split('d')

    assumedLatDe = newassumedLat[0]
    assumedLatMin = newassumedLat[1]
    assumedLongDe = newassumedLong[0]
    assumedLongMin = newassumedLong[1]

    lat = values['lat']
    long = values['long']
    altitude = values['altitude']


    LHA = degreeToMinute(lat) + degreeToMinute(assumedLat)
    intermediateDistance = (math.sin(math.radians(degreeToMinute(lat))) * math.sin(math.radians(degreeToMinute(assumedLat)))) + (math.cos(math.radians(degreeToMinute(lat))) * math.cos(math.radians(degreeToMinute(assumedLat))) * math.cos(math.radians(LHA)))
    correctedAltitude = math.degrees(math.asin(intermediateDistance))   #something wrong
    correctedDistance = degreeToMinute(altitude) - correctedAltitude
    values['correctDistance'] = minuteToDegree(correctedDistance)

    Azimuth1 = math.sin(math.radians(degreeToMinute(lat))) - (math.sin(math.radians(degreeToMinute(assumedLat))) * intermediateDistance)
    Azimuth2 = math.cos(math.radians(degreeToMinute(assumedLat))) * math.cos(math.asin(intermediateDistance))
    correctedAzimuth = math.acos(Azimuth1 / Azimuth2)
    values['correctedAzimuth'] = minuteToDegree(correctedAzimuth)



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

