"""
    Created on Feb 5, 2017
    @author: Linyuan Zhang
"""
from __future__ import print_function
import urllib

def convertString2Dictionary(inputString = ""):
    errorDict = {'error':'true'}
    outPut = {}         # A vaild output container.
    inputString = urllib.unquote(inputString)
    # Separate input string with ',' and remove space between elements.
    keyValues = inputString.split(',')
    keyValues = [str1.strip() for str1 in keyValues]
    if len(keyValues) == 0:       # There is at least one key value pair.
        return errorDict
    # Separate each pair with '=' as and remove space between elements.
    for str2 in keyValues:
        keyValue = str2.split('=')
        keyValue = [str3.strip() for str3 in keyValue]
        # check that each pair have a 'key' and a 'value'
        if len(keyValue) != 2:
            return errorDict
        key = keyValue[0]
        if len(key) <= 0:
            return errorDict
        if not key.isalnum():        # check key are alphanumeric
            return errorDict
        if not key[:1].isalpha():    # check key is not begin with digit
            return errorDict
        if key in outPut:            # check key is not duplicate
            return errorDict
        value = keyValue[1]          #check value is valid
        if len(value) == 0:
            return errorDict
        outPut[key] = value
    return outPut


