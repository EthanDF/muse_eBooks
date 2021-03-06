#__author__ = 'staff'

import urllib
from urllib import request
import csv
import tkinter
import os

# r = requests(testurl)

root = tkinter.Tk()
root.withdraw()

def checkForAccess(requestText):
    """given a request text result - review for access"""
    accessText = 'title_access_icon" class="access_yes">'

    a = -1
    if accessText in requestText:
        #access yes
        a = 1
    else:
        #access no
        a= 0

    return a

def testMuseURL(url):
    """checks for the response and the accuracy of a given MUSE URL"""

    requestResult = []
    result = 0
    r = urllib.request.urlopen(url)

    rcode = r.code
    # print(rcode)

    if rcode != 200:
        result = 0

    # print(r.url)
    if r.url == 'https://muse.jhu.edu/' or r.url == 'http://muse.jhu.edu/':
        result = 1
    else:
        result = 2

    rBinary = r.readall()
    accessResult = checkForAccess(rBinary.decode())

    requestResult = [result, accessResult]

    return requestResult



def loadtests(csvFile):
    museFile = csvFile
    museList = []
    with open(museFile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            museList.append(row)

    return museList

def logResults(resultList):
    """writes a result list to a log file"""
    resultsFile = 'logresults.csv'

    import time
    now = time.strftime('%Y-%m-%d %H:%M:%S')

    sysID = resultList[0]
    ctrlnum = resultList[1]
    url = resultList[2]
    urlResult = resultList[3]
    accessResult = resultList[4]

    data = [[now,str(sysID), str(ctrlnum), str(url), str(urlResult), str(accessResult)]]

    # print (data)
    # resultsFile = 'c:\\users\\fenichele\\desktop\\resultsFile.csv'
    with open(resultsFile, 'a', newline='') as out:
        a = csv.writer(out, delimiter=',', quoting=csv.QUOTE_ALL)
        a.writerows(data)

def museeBook():
    testurl = 'https://muse.jhu.edu/books/9781631011566/'

    from tkinter import filedialog
    marcPath = tkinter.filedialog.askopenfile()
    marcFile = marcPath.name

    museList = loadtests(marcFile)

    for a in museList:
        outcome =[]
        # bib = a[0]
        # utl = a[1]
        # testurl = a[2]

        # print(testurl)

        result = 0
        result = testMuseURL(a[2])

        if result[0] == 2:
            pass
            # print("no problem")
        elif result[0] == 1:
            print(a[2], "URL Resolves to MUSE Homepage")
        elif result[0] == 0:
            print("Invalid URL")
        else:
            print ("unknown result")

        outcome = [a[0],a[1],a[2],result[0],result[1]]

        logResults(outcome)
    print('...done')
    input('press any key to launch the log file')
    os.system("start "+'logresults.csv')

museeBook()