import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
import time

def create_df():

    links = []
    names = []
    prices = []
    times = []
    places = []
    users = []
    ratings = []

    for i in range(0, 1500, 50):
        url = 'https://hardverapro.hu/aprok/hardver/videokartya/index.html?offset={}'.format(i)
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req, timeout=20).read()
        time.sleep(0.2)
        soup = BeautifulSoup(resp, 'lxml')

        # f = open("test.xml", "a+", encoding="utf-8")
        # f.write(str(soup))
        # f.close()

        link_list = soup.find_all('a', {'class':'uad-image align-self-center'})
        price_list = soup.find_all('div', {'class':'uad-price'})
        time_list = soup.find_all('div', {'class':'uad-ultralight'})
        temp_list = soup.find_all('div', {'class':'uad-light'})
        rating_list = soup.find_all('span', {'class': 'uad-rating'})

        place_list = []
        user_list = []
        for k in range(0, len(temp_list), 3):
            place_list.append(temp_list[k].text)
            user_list.append(temp_list[k+1].text)

        if not link_list:
            break
        else:
            for j in range(len(link_list)):
                link = link_list[j]['href']
                name = soup.find_all('a', {'href': link})[1].text
                if price_list[j].text[-3:] == ' Ft':
                    price = int(price_list[j].text[:-3].replace(' ',''))
                else:
                    price = price_list[j].text
                links.append(link)
                names.append(name)
                prices.append(price)
                times.append(time_list[j].text)
                places.append(place_list[j])
                users.append(user_list[j])
                ratings.append(rating_list[j].text)

    df = pd.DataFrame()
    df['Link'] = links
    df['Name'] = names
    df['Price'] = prices
    df['Place'] = places
    df['Time'] = times
    df['User'] = users
    df['Rating'] = ratings

    return df

df = create_df()
df.to_excel('VGA.xlsx', encoding="utf-8", index=False)

