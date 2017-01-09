#!/usr/bin/env python3

import urllib.parse, urllib.request

mediacorp_test_domains = [ "http://www.google.com",
                           "http://www.google.com.sg",
                           "http://www.yahoo.com.sg",
                           "http://channelnewsasia.com",
                           "http://www.ibm.com"]



def test_url(url):
    print("Testing {}".format(url))

    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(">>> Error code {}".format(e.code))
    except urllib.error.URLError as e:
        print(">>> Unable to fetch page")
    else:
        print(">>> Return code is 200")




for d in mediacorp_test_domains:
    test_url(d)

