import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
import time
import random

url_address = 'https://www.hasznaltauto.hu/talalatilista/PCOG2VG3N3RDAEH5C57UARICFHKH3XCVWWKVMVNFSX5BUDLEBATLMB6ZJZKKR6XPHN3FESAALYMM35OM6GMYBHB7ZEXS7M24RIDAFVXECS6GCJ463GLUTYKPNBIB7IINSROAWKKAJ4J57WF7SJRE3HIKDBBO7CFVDUDNJYCKUNWKY7MUMJPMZ6BHV3R7AOOEK6LXQIIFW2XJZ5FI4TJXF5VQZJTZOX3RF437NK3EHYXZMD6LNRAL2A37WKQEHOIHM7NDIQUKFT6S7JNIYGA52KGQZLPUTSBDB6QMTXUJ6HWDKOWUHMGHIJY4E4VVOMJS35A4KGGE6NNM4JQRPKAX3AB5BTCM3JGY6INJZ6222GC4ZQOXCNY6HDA3I4T27YWQW45PQOD5ZYUAMOSX244H46NXDUNBLCM5H5SPAH52JZWTAFJTBZY6D3T5O52GIP2UQU2OZF724ZWGYWQ7ZD6FKPV4HMZBIFGZ25VNJYJRGX4HQ7I3C5TE6URI77RPUQTF5ML2KA52GF3QZWMANOQFJY3OLRT2QQVNSN55AXSQQ7LO6UMPOFZRX3HYIEQPYCEQG5Q6SLDOUK67YURUZNC46YVDUKNCODKZAVNT5AYQDIZZE5EWT4STWSJYNM5D6JZQ6SLM6CPMCHVFDY3FHQUQ2B7C2MAVTSBP2UFSJUNAMTLNW6NU6PPJ4R3333NYW2BPPK5RBT67NTYLH36Q23UFU5667VTYS2NMA44WFDEVJBG4SYRXOC2XVK6R4NWYQ53C3Y2ZUEZVCE7A76CKJ4JL6GAGAKGB7HMTZH5VHQ7X2KGP3D2RBO2FLHYTQWYBONJWEGFMVF5Q2YYCTCRTOTFROYGV3DGWE3VUGJYJKGWQDQRJ5SMEOTLVD4VHQ3WLCG6HTAT7JBZL6AOVTWURUN5NFBO7R552APNCF636I2WQM2BGRWL75H4AG455D2PUK6KIQ5KXNU6L7LXJ7AYTP3J2MNLII7AL77YDC2G33QI/page{}'


def GET_UA():

    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
        ]

    return random.choice(uastrings)


def create_df():

    links = []
    names = []
    prices = []
    times = []
    places = []
    users = []
    ratings = []

    for i in range(1, 20, 1):

        random.uniform(0.01, 0.2)
        url = url_address.format(i)
        req = Request(url,  headers={'User-Agent': GET_UA()})
        resp = urlopen(req, timeout=20).read()
        time.sleep(0.1)
        soup = BeautifulSoup(resp, 'lxml')

        # f = open("test.xml", "w+", encoding="utf-8")
        # f.write(str(soup))
        # f.close()

        temp_list = soup.find_all('h3')
        for t in range(len(temp_list)):
            if len(temp_list[t].find_all('a', {'class': ''}))>0:
                links.append(temp_list[t].find_all('a', {'class': ''})[0]['href'])
                names.append(temp_list[t].find_all('a', {'class': ''})[0].text)

