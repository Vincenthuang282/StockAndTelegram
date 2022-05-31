from bs4 import BeautifulSoup
import requests as req
from urllib import parse
from datetime import datetime

def weather(location):
    now_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    city=location
    number={
        '臺北':'2306179',
        '新北':'20070569',
        '基隆':'2306188',
        '桃園':'2298866',
        '新竹':'2306185',
        '苗栗':'2301128',
        '台中':'2306181',
        '彰化':'2306183',
        '南投':'2306204',
        '雲林':'2347346',
        '嘉義':'2296315',
        '台南':'2306182',
        '高雄':'2306180',
        '屏東':'2306189',
        '宜蘭':'2306198',
        '花蓮':'2306187',
        '臺東':'2306190',
        '澎湖':'28760737',
        '綠島':'2301301',
        '蘭嶼':'2300334',
        '福建':'12517930',
        '馬祖':'12517946',
    }  ##this is the value that i want to specify
    country='臺灣'

    #print(location)

    query=parse.quote(country+'/'+city+'/'+city+'-'+number[city])
    list=[]
    url='https://tw.news.yahoo.com/weather/'+query
    html=req.get(url)
    soup=BeautifulSoup(html.text,'html.parser')
    result_temparature_highiest_lowest=soup.findAll('span',attrs={'class':'Va(m) Px(6px)'})
    for result in result_temparature_highiest_lowest:
        list.append(result.text)
    list.append(soup.find('span',attrs={'data-reactid':'37'}).text)
    list.append(soup.find('div',attrs={'data-reactid':'409'}).text)
    list.append(soup.find('div',attrs={'data-reactid':'412'}).text)

    return city+"\n"+now_time[0:10]+"\n當日最高溫度:"+list[0]+"\n當日最低溫度:"+list[1]+"\n現在溫度:"+list[2]+"°\n現在體感溫度:"+list[3]+"\n現在濕度:"+list[4]
