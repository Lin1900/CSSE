import math
import datetime
import re
import os

stars = {
    'Alpheratz': '357d41.7,29d10.9',
    'Ankaa': '353d14.1,-42d13.4',
    'Schedar': '349d38.4,56d37.7',
    'Diphda':'348d54.1,-17d54.1',
    'Achernar':	'335d25.5,-57d09.7',
    'Hamal': '327d58.7,23d32.3',
    'Polaris':'316d41.3,89d20.1',
    'Akamar':'315d16.8,-40d14.8',
    'Menkar':'314d13.0,4d09.0',
    'Mirfak':'308d37.4,49d55.1',
    'Aldebaran':	'290d47.1,16d32.3',
    'Rigel':	'281d10.1,-8d11.3',
    'Capella':	'280d31.4,46d00.7',
    'Bellatrix':	'278d29.8,6d21.6',
    'Elnath':	'278d10.1,28d37.1',
    'Alnilam':	'275d44.3,-1d11.8',
    'Betelgeuse':'270d59.1,7d24.3',
    'Canopus':	'263d54.8,-52d42.5',
    'Sirius':	'258d31.7,-16d44.3',
    'Adara':	'255d10.8,-28d59.9',
    'Procyon':	'244d57.5,5d10.9',
    'Pollux':	'243d25.2,27d59.0',
    'Avior':	'234d16.6,-59d33.7',
    'Suhail':'222d50.7,-43d29.8',
    'Miaplacidus':	'221d38.4,-69d46.9',
    'Alphard':	'217d54.1,-8d43.8',
    'Regulus':	'207d41.4,11d53.2',
    'Dubhe':	'193d49.4,61d39.5',
    'Denebola':	'182d31.8,14d28.9',
    'Gienah':	'175d50.4,-17d37.7',
    'Acrux':	'173d07.2,-63d10.9',
    'Gacrux':	'171d58.8,-57d11.9',
    'Alioth':'166d19.4,55d52.1',
    'Spica':	'158d29.5,-11d14.5',
    'Alcaid':	'152d57.8,49d13.8',
    'Hadar':	'148d45.5,-60d26.6',
    'Menkent':'148d05.6,-36d26.6',
    'Arcturus':	'145d54.2,19d06.2',
    'Rigil Kent.':'139d49.6,-60d53.6',
    'Zubenelg.':	'137d03.7,-16d06.3',
    'Kochab':	'137d21.0,74d05.2',
    'Alphecca':'126d09.9,26d39.7',
    'Antares':	'112d24.4,-26d27.8',
    'Atria':	'107d25.2,-69d03.0',
    'Sabik':	'102d10.9,-15d44.4',
    'Shaula'	:'96d20.0,-37d06.6',
    'Rasalhague':	'96d05.2,12d33.1',
    'Etamin'	:'90d45.9,51d29.3',
    'Kaus Aust.':	'83d41.9,-34d22.4',
    'Vega'	:'80d38.2,38d48.1',
    'Nunki'	:'75d56.6,-26d16.4',
    'Altair'	:'62d06.9,8d54.8',
    'Peacock'	:'53d17.2,-56d41.0',
    'Deneb'	:'49d30.7,45d20.5',
    'Enif'	:'33d45.7,9d57.0',
    'Alnair'	:'27d42.0,-46d53.1',
    'Fomalhaut'	:'15d22.4,-29d32.3',
    'Scheat'	:'13d51.8,28d10.3',
    'Markab'	:'13d36.7,15d17.6'
}


def Predict(values):
    if not 'body' in values:
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
    if 'date' in values:
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
        if not month.isdigit() or int(month) >12 or int(month) < 0:
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
        elif month == 2 and year % 4 == 0:     #check leap year
            if day != 29:
                values['error'] = 'date is invalid'
                return values
        elif month == 02 and year % 4 != 0:
            if day != 28:
                values['error'] = 'date is invalid'
                return values
        else:
            if day != 30:
                values['error'] = 'date is invalid'
                return values

    if 'time' not in values:
        values['time'] = '00:00:00'
    if 'time' in values:
        time = values['time'].split(':')
        if len(time) != 3:
            values['error'] = 'time is invalid'
            return values
        # check hour valid or not
        hour = time[0]
        if not hour.isdigit() or len(hour) != 2:
            values['error'] = 'time is invalid'
            return values
        if int(hour) >= 24 or int(hour) < 0:
            values['error'] = 'time is invalid'
            return values
        # check minutes valid or not
        minute = time[1]
        if not minute.isdigit() or len(minute) != 2:
            values['error'] = 'time is invalid'
            return values
        if int(minute) > 60 or int(minute) < 0:
            values['error'] = 'time is invalid'
            return values
        # check second valid or not
        second = time[2]
        if not second.isdigit() or len(second) != 2:
            values['error'] = 'time is invalid'
            return values
        if int(second) > 60 or int(second) < 0:
            values['error'] = 'time is invalid'
            return values


    #getStar = read_file(values['body'])
    #if (getStar == -1):
     #   values['error'] = "star not in catalog"
      #  return values

    GHA = '100d42.6'
    SHA = getStar[1]
    latitude = getStar[2]
    gapYear = year - 2001
    diffAngular = gapYear * degreeToMinute('-0d14.31667')
    countLeapYear = gapYear / 4
    dailyRotation = abs(degreeToMinute('360d0.00') - (86164.1/86400) * degreeToMinute('360d00.0'))
    totalPro = dailyRotation * countLeapYear
    nowGHA = degreeToMinute(GHA) + diffAngular + totalPro
    totalSecond1 = int(second) + int(minute) * 60 + int(hour) * 3600
    epoch = datetime(year, 1, 1)
    now = datetime(year, month, day)
    totalSecond2 = (now - epoch).total_second
    totalSecond = totalSecond1 + totalSecond2
    countRotation = totalSecond / (86164.1) * degreeToMinute('360d00.0')
    newGHA = nowGHA + countRotation
    starGHA = newGHA + degreeToMinute(SHA)
    newStarGHA = minuteToDegree(starGHA)
    values['long'] = newStarGHA
    values['lat'] = latitude
    return values

"""
def read_file(star):
    filePath = os.path.dirname(__file__)
    Stars = open(filePath + '/stars.txt')
    for i in range(0, 60):
        line = Stars.readline()
        newLine = line.split()
        if (newLine[0].lower() == star.lower()):
            return newLine
    Stars.close()
    return -1
"""

def degreeToMinute(d):
    degree = d.split('d')
    hour = int(degree[0])
    minute = float(degree[1])
    if hour != 0:
        if hour > 0:
            newDegree = hour + minute/60
        else:
            newDegree = hour - minute/60
    else:
        newDegree = abs(minute/60)
    return newDegree

def minuteToDegree(m):
    degree = str(m).split('.')
    hour = int(degree[0])
    minute = (m - hour) * 60
    newm = str(hour) + 'd' +str(minute)
    return newm





