import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date

def create_df(date):

    flats_df = pd.DataFrame()
    links = []
    prices = []
    price_per_sqms = []
    addresses = []
    areas = []
    rooms = []

    for i in range(1, 100):
        url = 'https://ingatlan.com/szukites/elado+lakas+uj-epitesu+tegla-epitesu-lakas+ujszeru+iii-ker+40-60-m2+foldszint-10-felett-emelet?page={}'.format(i)
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req, timeout=20).read()
        soup = BeautifulSoup(resp, 'lxml')


        link_list = soup.find_all('a', {'class' : 'listing__link js-listing-active-area'})
        price_list = soup.find_all('div', {'class' : 'price'})
        price_per_sqm_list = soup.find_all('div', {'class' : 'price--sqm'})
        address_list = soup.find_all('div', {'class' : 'listing__address'})
        area_list = soup.find_all('div', {'class' : 'listing__parameter listing__data--area-size'})
        room_list = soup.find_all('div', {'class' : 'listing__parameter listing__data--room-count'})

        if not link_list:
            break
        else:
            for i in range(len(link_list)):
                links.append("https://ingatlan.com" + link_list[i]['href'])
                prices.append(float(price_list[i].text[:-6]))
                price_per_sqms.append(int(price_per_sqm_list[i].text[:-7].replace(' ', '')))
                addresses.append(address_list[i].text)
                areas.append(int(area_list[i].text[:-11]))
                rooms.append(room_list[i].text[:-6])

    flats_df['Link'] = links
    flats_df['Cím'] = addresses
    flats_df['Terület [m2]'] = areas
    flats_df['Szobák'] = rooms
    flats_df['[MFt] {}'.format(date)] = prices
    flats_df['[Ft/m2] {}'.format(date)] = price_per_sqms

    return flats_df

# flats_df = create_df(date.today())
# flats_df.to_excel('Flats.xlsx', encoding="utf-8", index=False)