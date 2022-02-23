import re
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

data = []
for i in range (102,158):
    URL = 'http://bulibox.de/abschlusstabellen/'
    URL_ = URL + 'B100' +str(i+1) + '.html'
    r = urllib.request.urlopen(URL_).read()
    soup = BeautifulSoup(r,'lxml')
    table = soup.find('table' ,attrs={'class':'abschluss'})
    body = table.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    headings = []
    for item in head.find_all('th'):
        item = (item.text).rstrip('\n')
        headings.append(item)
    all_rows = [] 
    for row_num in range(len(body_rows)):
        row = []
        for row_item in body_rows[row_num].find_all("td"):
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)
    df1 = pd.DataFrame(data=all_rows,columns=headings)
    data.append(df1)

df = pd.concat(data)

df.to_csv(r'C:\Users\tobis\OneDrive\Desktop\BuliBox.csv')