from matplotlib.font_manager import FontManager, FontProperties
import matplotlib.pyplot as plt
import seaborn as sb
import csv
import numpy as np
from fuzzywuzzy import fuzz
import os

def PictureMaker(input):
    status=[]
    status_reverse=[]
    stockname=[]
    file_name=[]
    selects=[]
    dir = r"C:\Users\VINCENT\OneDrive\桌面\Feb(SockAndTelegram)\Stock\result_file"
    for row in os.listdir(dir):
        file_name.append(row[:-4])
    for search in input:
        for row in file_name:
            if fuzz.partial_ratio(search,row) > 70:
                selects.append(row)




    for k in range(0,len(selects),1):
        ChineseFont1 = FontProperties(fname = 'C:\\Windows\\Fonts\\simsun.ttc')
        a=open("./result_file/"+selects[k]+'.csv','r',encoding='utf-8',newline='')
        reader=csv.reader(a)
        status.append([])
        status_reverse.append([])
        date=[]
        for row in reader:
            status[k].append(int(row[4])/10)
            date.append(row[0])
            name=row[1]

        for i in range(0,len(date),1):
            status_reverse[k].append(status[k][len(date)-i-1])


        stockname.append(name)
    heat_map=sb.heatmap(status_reverse,cmap='Reds',cbar=False,linecolor='white',linewidths=1,annot=False)
    y_ticks=np.arange(len(stockname))
    plt.yticks(y_ticks,rotation=0,fontsize=10) #fontsize

    for i in range(0,len(heat_map.get_yticklabels()),1):
        y=heat_map.get_yticklabels()
        y[i]=stockname[i][:-2]  
        heat_map.set_yticklabels(y,fontproperties=ChineseFont1)

    x_ticks=np.arange(len(date))      
    plt.xticks(x_ticks,rotation=90,fontsize=5)   #fontsize

    for i in range (0,len(heat_map.get_xticklabels()),1):
        x=heat_map.get_xticklabels()
        x[i]=date[len(heat_map.get_xticklabels())-i-1]
        heat_map.set_xticklabels(x)

    
    plt.title("指數溫度圖",fontproperties=ChineseFont1,x=0.5,y=1.03)

    plt.tight_layout()
    plt.savefig("./picture/result.jpg")
    #plt.show()