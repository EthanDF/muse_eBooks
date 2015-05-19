#__author__ = 'staff'

import requests
import csv

# r = requests(testurl)

def testMuseURL(url):
    """checks for the response and the accuracy of a given MUSE URL"""

    result = 0
    r = requests.get(testurl, verify=False)

    rcode = r.status_code
    print(rcode)

    if rcode != 200:
        result = 0

    print(r.url)
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

def museeBook():
    testurl = 'https://muse.jhu.edu/books/9781631011566/'

    museList = loadtests()

    for a in museList[0:10]:
        outcome =[]
        bib = a[0]
        utl = a[1]
        testurl = a[2]

        print(testurl)

        result = 0
        result = testMuseURL(testurl)
        if result == 2:
            print("no problem")
        elif result == 1:
            print("URL Resolves to MUSE Homepage")
        elif result == 0:
            print("Invalid URL")
        else:
            print ("unknown result")

        outcome = [bib,utl,testurl,result]

        print (outcome)
