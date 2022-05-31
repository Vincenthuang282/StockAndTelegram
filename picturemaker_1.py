from matplotlib.font_manager import FontManager, FontProperties
import matplotlib.pyplot as plt
import seaborn as sb
import csv
import numpy as np
from fuzzywuzzy import fuzz
import os


#############----------------------------List the File The User Want--------------------------------------------##################################
def PictureMaker(input,day):
    print(input)
    print(day)
    status=[]
    status_reverse=[]
    value=[]
    stockname=[]
    file_name=[]
    selects=[]
    if(day=='30'):
        size=10
        days=30
    elif(day=='45'):
        size=6
        days=45
    elif(day=='60'):
        size=4
        days=60
    dir = r"C:./result_file"
    for row in os.listdir(dir):
        file_name.append(row[:-4])
    for search in input:
        if(search=="*"):
            for row in file_name:
                selects.append(row)
    
        else:
            for row in file_name:
                if (row not in selects )and (fuzz.partial_ratio(search,row))>70:
                    selects.append(row)
#############------------------------------------------------------------------------##################################  
    
    data={}
    sorted_data={}
    arr=[]
    for k in range(0,len(selects),1):
        ChineseFont1 = FontProperties(fname = r'./SIMSUN.TTC')
        a=open(r"./result_file/"+selects[k]+'.csv','r',encoding='utf-8',newline='')
        reader=csv.reader(a)
        status.append([])
        status_reverse.append([])
        date=[]
        
        for row in reader:
            status[k].append(int(row[4])/10)
            date.append(row[0])
            name=row[1]
        stockname.append(name)
        for i in range(0,len(date),1):
            status_reverse[k].append(status[k][len(date)-i-1])
###########------------------Sorted The Data According to Their Heat From High to Low---------------------------------------------#############################
    for i in range(0,len(stockname),1):
        for k in range(i+1,len(stockname),1):
            if(status_reverse[i][len(date)-1]<status_reverse[k][len(date)-1]):
                temp=status_reverse[i]
                status_reverse[i]=status_reverse[k]
                status_reverse[k]=temp
                stock_temp=stockname[i]
                stockname[i]=stockname[k]
                stockname[k]=stock_temp
##################------------------------------------------------------------------############################
    for i in range(0,len(status_reverse),1):
        value.append([]) 
        value[i]=status_reverse[i][-int(days):] ###---------------------------------------->>>>>>>the Places to change the len(date) 
       
##################------------------------------------------------------------------############################

    heat_map=sb.heatmap(value,cmap='Reds',cbar=False,linecolor='white',linewidths=1,annot=False)
    y_ticks=np.arange(len(stockname))
    plt.yticks(y_ticks,rotation=0,fontsize=10) #fontsize
    for i in range(0,len(heat_map.get_yticklabels()),1):
        y=heat_map.get_yticklabels()
        y[i]=stockname[i][:-2]  
        heat_map.set_yticklabels(y,fontproperties=ChineseFont1)
    x_ticks=np.arange(int(days))  ###---------------------------------------->>>>>>>the Places to change the len(date)     
    plt.xticks(x_ticks,rotation=90,fontsize=size)   #fontsize
    for i in range (0,len(heat_map.get_xticklabels()),1):
        x=heat_map.get_xticklabels()
        x[i]=date[len(heat_map.get_xticklabels())-i-1]
        heat_map.set_xticklabels(x)
    plt.title("指數溫度圖",fontproperties=ChineseFont1,x=0.5,y=1.03)
    plt.tight_layout()
    plt.savefig(r"./picture/result.jpg")
    plt.close()
    #plt.show()
