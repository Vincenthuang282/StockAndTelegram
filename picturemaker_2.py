
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def PictureMaker2(day):
    a=open("/home/vincenthuang282/StockAndTelegram/result_file/發行量加權股價指數.csv","r",encoding="utf-8",newline="")
    reader=csv.reader(a)
    Date=[]
    Date_reverse=[]
    Date_value=[]
    Price=[]
    Price_reverse=[]
    Price_value=[]
    if(day=='30'):
        size=10
        days=30
    elif(day=='45'):
        size=6
        days=45
    elif(day=='60'):
        size=5
        days=60
    for row in reader:
        Price.append(float(row[2]))
        Date.append(row[0])
    for k in range (0,len(Date),1):
        Date_reverse.append(Date[len(Date)-k-1])
        Price_reverse.append(Price[len(Price)-k-1])
    for k in range (len(Date)-1-int(days),len(Date),1):
        Date_value.append(Date_reverse[k])
        Price_value.append(Price_reverse[k])



    ChineseFont1 = FontProperties(fname = '/home/vincenthuang282/StockAndTelegram/SIMSUN.TTC')
    plt.plot(Date_value,Price_value,"r-o",label='Price')
    plt.title("台灣加權指數",fontproperties=ChineseFont1,x=0.5,y=1.03)
    plt.xticks(fontsize=size,rotation=90)
    plt.yticks(fontsize=10)
    plt.xlabel("Date",fontsize=10,labelpad=2)
    plt.ylabel("Price",fontsize=10,labelpad=2)
    plt.legend(loc="best",fontsize=10)
    plt.tight_layout()
    plt.savefig("/home/vincenthuang282/StockAndTelegram/picture/result2.jpg")
    plt.close()
    ##plt.show()
