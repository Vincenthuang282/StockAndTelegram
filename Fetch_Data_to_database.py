import time
from datetime import datetime,timedelta
from urllib import response
from urllib.request import urlopen
import json
import sqlite3



#conn=sqlite3.connect('test.db')
#c=conn.cursor()
#c.execute("drop table stocks")
#c.execute(' CREATE TABLE stocks (Date text, Stock_Name text , Price real) ')
#c.execute("delete from stocks where rowid not in (select min(rowid) from stocks group by Date,Stock_Name,Price)")
#conn.commit()
#result=c.execute("select * from stocks where Stock_Name='化學生技醫療類指數'")
#for row in result:
#    print(row)
#conn.close()    
#c.execute(' CREATE TABLE stocks (Date text, Stock_Name text , Price real) ')
#c.execute("delete from stocks where Price=3.0")
#
conn=sqlite3.connect('/home/vincenthuang282/StockAndTelegram/test.db')
c=conn.cursor()
for d in range(0,10,1):
    print(d)
    now=datetime.now()
    date_time= datetime.now()-timedelta(days=d)
    date_time=date_time.strftime("%Y%m%d")
    url='https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date='+date_time+'&type=IND&_=1643276494643'
    response=urlopen(url)
    data_json=json.loads(response.read())

    try:
        for i in range (0,len(data_json['data1']),1):
            name=data_json['data1'][i][0]
            price=float(''.join([i for i in data_json['data1'][i][1] if not i==',']))
            c.execute('insert into stocks VALUES(?,?,?)',(date_time,name,price))  


        

        result=c.execute("select * from stocks")

        for row in result:
            print(row)

        

        print("--------------------------------------------------------------")
        
    except:
        pass
    if(d%6==5):
        time.sleep(60)
c.execute("delete from stocks where rowid not in (select min(rowid) from stocks group by Date,Stock_Name,Price)") ##delete the same data
conn.commit() 
conn.close()
