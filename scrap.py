import requests
from bs4 import BeautifulSoup
url='https://coinmarketcap.com'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')

table_row=soup.find_all('tr')
table_row.pop(0)



def fun():
    datas=[]
    for row in table_row:
        col=row.find_all('td')
        link=col[2].find('a')
        a=link.get('href')
        img=col[2].find('img')
        logo=None
        if img is not None:
            logo=img['src']
        else:
             logo='static/coin.png'
        val={'name':col[2].get_text(),
            'price':col[3].get_text(),
            'url':url+a,
            'logo':logo
            }
        datas.append(val)
    return datas

# for data in datas:
#     print(data)

fun()