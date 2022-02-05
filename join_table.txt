import pandas as pd
import new_table as new
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
import openpyxl as xl

today = date.today()

flats_file = "C:\Python\Projects\WebScraping\Flats.xlsx"
price_df = pd.read_excel(flats_file, sheet_name = 'Ár')

new_df = new.create_df(today)

new_price_df = new_df.drop(columns = ['[Ft/m2] {}'.format(today)])

price_df = price_df.set_index('Link').join(new_price_df.set_index('Link'), how = 'outer', rsuffix = '_right')
price_df['Cím'] = price_df['Cím'].fillna(price_df['Cím_right'])
price_df['Terület [m2]'] = price_df['Terület [m2]'].fillna(price_df['Terület [m2]_right'])
price_df['Szobák'] = price_df['Szobák'].fillna(price_df['Szobák_right'])
price_df = price_df.drop(columns = ['Cím_right', 'Terület [m2]_right', 'Szobák_right', '[eFt/nm]'])
price_df['[eFt/nm]'] = round((price_df['[MFt] {}'.format(today)]*1000000 / price_df['Terület [m2]']/1000), 3)

writer = pd.ExcelWriter(flats_file, engine='xlsxwriter')
price_df.to_excel(writer, sheet_name = 'Ár', encoding='utf-8')

writer.save()

print('Data has been downloaded for {} and has been saved to the following file: {}'.format(today, flats_file))