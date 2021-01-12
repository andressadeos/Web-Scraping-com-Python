import requests
import os
import openpyxl
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://www.amazon.com.br/s?k=iphone&ref=nb_sb_noss'
res = requests.get(url)
res.encoding = 'utf-8'
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser') # transformando em objeto
print(type(soup)) 

list = soup.find_all('div', class_='s-result-item')
print(len(list))

first_result = list[8]
print(first_result)

first_name = first_result.h2.a.text
print(first_name)

first_price = first_result.find('span', class_='a-offscreen').getText()
print(first_price)

price_null = list[8].find('span', class_='a-price)')
print(type(price_null))

#list
prices = []
names = []

for all_list in list:
  if all_list.find('span', class_='a-price') is not None:
    
    name= all_list.h2.a.text
    names.append(name)

    price=all_list.find('span', class_='a-offscreen').getText()
    prices.append(price)


df=pd.DataFrame({'product':names, 'price':prices})
print(df.info())

os.chdir('C:\\Andressa\\workspace\\WEB SCRAPING AMAZOM - IPHONE') #diretorio para salvar
df.to_excel('amazoniphone.xlsx',index=False) #nome do aqrqivo