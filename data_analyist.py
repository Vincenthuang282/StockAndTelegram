import csv 
import sqlite3

index_type=[]
stock_info_price=[]
stock_info_date=[]
stock_info_name=[]
count=0
conn =sqlite3.connect('/home/vincenthuang282/StockAndTelegram/test.db')
c=conn.cursor()
result=c.execute("select * from stocks group by Stock_Name")
for row in result:
    index_type.append(row[1])
for stock_name in index_type:    
    stock_info = c.execute("select * from stocks where Stock_Name='%s' order by Date DESC" % stock_name)
    for row in stock_info:
        stock_info_date.append(row[0])
        stock_info_name.append(row[1])
        stock_info_price.append(row[2])
    for i in range(0,len(stock_info_date)-20,1):
        sum=0
        average=0
        now_price=stock_info_price[i]
        for k in range (i,i+20,1):
            sum=stock_info_price[k]+sum
            average=sum/20
        d=average*0.01
        d2=d*2
        if(now_price<(average+d)) and (now_price>(average-d)):
            status='3'
            sum=0
        elif(now_price>(average-d2)) and (now_price<(average-d)):
            status='2'
            sum=0
        elif(now_price<(average+d2)) and (now_price>(average+d)):
            status='4'
            sum=0
        elif(now_price<(average-d2)):
            status='1'
            sum=0
        elif(now_price>(average+d2)):
            status='5'
            sum=0
        ##print(stock_info_name[i]+" "+str(stock_info_date[i])+" "+str(stock_info_price[i])+" "+str(average)+" "+status)
        a=open("/home/vincenthuang282/StockAndTelegram/result_file/"+stock_info_name[i]+'.csv','a',encoding='utf-8',newline='')
        writer_a=csv.writer(a)
        writer_a.writerow([stock_info_date[i],stock_info_name[i],stock_info_price[i],average,status])
    stock_info_price=[]
    stock_info_date=[]
    stock_info_name=[]
conn.close()

