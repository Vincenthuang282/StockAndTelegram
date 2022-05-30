from bs4 import BeautifulSoup
import requests as req


def stock(stock_name):
    stock_name="TSLA"
    count=1
    list=[]
    url='https://finance.yahoo.com/quote/'+stock_name
    news_url='https://finance.yahoo.com'
    html=req.get(url)
    soup=BeautifulSoup(html.text,'html.parser')
    news=soup.findAll('a',{"class":"js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled"})
    for new in news:
        if count>6:
            break
        count=count+1
        list.append({'title':new.text,'url':news_url+new['href']})
    ##print(list)
    return list
##
##for new in stock('NVDA'):
##    print(new['title']+" "+new['url'])