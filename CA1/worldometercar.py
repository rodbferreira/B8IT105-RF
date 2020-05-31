# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:54:37 2020

@author: Rodolfo Laptop
"""

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'authority': 'www.worldometers.info',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.worldometers.info/',
    'accept-language': 'en,en-US;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'cookie': '__cfduid=d0cbdbfd220c9739f6c80b013d3feda511585997194; _fssid=69142ab4-bb9e-4d20-8bca-28e35af5e8d2; _ga=GA1.2.1045199037.1585997198; _gid=GA1.2.2021722470.1585997198; _fsuid=4410f9c2-338a-46f7-9ea1-79705bfd954f; _fsloc=?i=IE^&c=Dublin; __beaconTrackerID=y2552xfyt; __qca=P0-363876325-1585997203693; __gads=ID=d9c487de9f1fe626:T=1585997202:S=ALNI_Ma1sfnnIlNG-9a5Nvl0F0BpTPWenQ; fsbotchecked=true; fssts=false; __atuvc=3^%^7C14; __atuvs=5e886592b85b3060002',
}
def get_page_contents():
    response = requests.get('https://www.worldometers.info/cars/', headers=headers)
    return response.content

def convert_to_soup(content):
    return BeautifulSoup(content, 'html.parser')

def process_data(soup):
    tableContentCars = soup.find(class_='table-striped')
    output_rows = []
    
    for table_row in tableContentCars.findAll('tr'):
    
        columns = table_row.findAll('td')
        output_row = []
    	
        for column in columns:
            output_row.append(column.get_text())
                		
        output_rows.append(output_row)

    with open('D:/DBS/BIG DATA/CA1/worldometercar.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)
        print(output_rows)
     
def main():
    contents = get_page_contents()
    soup = convert_to_soup(contents)
    process_data(soup)

if __name__=='__main__':
    main()
    

   