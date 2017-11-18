from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import pandas as pd

def getFilmTable(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("err http")
        return e
    try:
        soup = BeautifulSoup(html,"lxml")
        return soup.find_all("table",class_="wikitable sortable")[0]
    except AttributeError as e:
        print("err atr")
        return e

film_table = getFilmTable('https://en.wikipedia.org/wiki/Ryan_Gosling')


Year=[]
Title=[]
Role=[]

header_row = True
for row in film_table.findAll("tr"):
    if not header_row:
        cells = row.findAll('td')
        index_of_title = 1
        if len(cells) == 3:
            index_of_title = 0
            last_inserted_year = Year[-1]
            Year.append(last_inserted_year)
        else:
            Year.append(cells[0].find(text=True))
        
        Title.append(cells[index_of_title].find(text=True))
        role = cells[index_of_title + 1].find(text=True)  
        if role == None
            Role.append(cells[index_of_title + 2].find(text=True))
        else:
            Role.append(role)
    header_row = False

df=pd.DataFrame(Year,columns=['Date'])
df['Title']=Title
df['Role']=Role
df
