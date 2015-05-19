#__author__ = 'staff'

import requests
import csv
import tkinter

# r = requests(testurl)

root = tkinter.Tk()
root.withdraw()

def testMuseURL(url):
    """checks for the response and the accuracy of a given MUSE URL"""

    result = 0
    r = requests.get(testurl, verify=False)

    rcode = r.status_code
    # print(rcode)

    if rcode != 200:
        result = 0

    # print(r.url)
    if r.url == 'http://muse.jhu.edu/':
        result = 1
    else:
        result = 2

    return result

def loadtests():
    museFile = 'museURLs.csv'
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

    data = [[now,str(sysID), str(ctrlnum), str(url), str(urlResult)]]

    # print (data)
    # resultsFile = 'c:\\users\\fenichele\\desktop\\resultsFile.csv'
    with open(resultsFile, 'a', newline='') as out:
        a = csv.writer(out, delimiter=',', quoting=csv.QUOTE_ALL)
        a.writerows(data)

def museeBook():
    testurl = 'https://muse.jhu.edu/books/9781631011566/'

    museList = loadtests()

    for a in museList:
        outcome =[]
        # bib = a[0]
        # utl = a[1]
        # testurl = a[2]

        # print(testurl)

        result = 0
        result = testMuseURL(a[2])
        if result == 2:
            pass
            # print("no problem")
        elif result == 1:
            print("URL Resolves to MUSE Homepage")
        elif result == 0:
            print("Invalid URL")
        else:
            print ("unknown result")

        outcome = [a[0],a[1],a[2],result]

        logResults(outcome)

museeBook()