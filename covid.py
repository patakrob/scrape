import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
import time

oldal_tol = 0
oldal_ig = 200

def create_df(oldal_tol, oldal_ig):

    szam = []
    nem = []
    kor = []
    betegseg = []

    for i in range(oldal_tol, oldal_ig):
        url = 'https://koronavirus.gov.hu/elhunytak?page={}'.format(i)
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req, timeout=20).read()
        time.sleep(0.2)
        soup = BeautifulSoup(resp, 'lxml')

        # f = open("test.xml", "a+", encoding="utf-8")
        # f.write(str(soup))
        # f.close()

        szam_lista = soup.find_all('td', {'class':'views-field views-field-field-elhunytak-sorszam'})
        nem_lista = soup.find_all('td', {'class':'views-field views-field-field-elhunytak-nem'})
        kor_lista = soup.find_all('td', {'class':'views-field views-field-field-elhunytak-kor'})
        betegseg_lista = soup.find_all('td', {'class':'views-field views-field-field-elhunytak-alapbetegsegek'})

        for j in range(len(szam_lista)):
            szam.append(szam_lista[j].text.split()[0])
            nem.append(nem_lista[j].text.split()[0])
            kor.append(kor_lista[j].text.split()[0])
            betegseg.append(' '.join(betegseg_lista[j].text.split()))

        print('{} oldal a {}-ból.'.format(i, (oldal_ig-oldal_tol)))

    df = pd.DataFrame()
    df['Szám'] = szam
    df['Nem'] = nem
    df['Kor'] = kor
    df['Betegség'] = betegseg


    return df

df = create_df(oldal_tol, oldal_ig)
df.to_excel('Covid.xlsx', encoding="utf-8", index=False)