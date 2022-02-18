from audioop import reverse
import csv
from turtle import color
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def PictureMaker2():
    a=open("./result_file/發行量加權股價指數.csv","r",encoding="utf-8",newline="")
    reader=csv.reader(a)
    Date=[]
    Date_reverse=[]
    Price=[]
    Price_reverse=[]
    for row in reader:
        Price.append(float(row[2]))
        Date.append(row[0])
    for k in range (0,len(Date),1):
        Date_reverse.append(Date[len(Date)-k-1])
        Price_reverse.append(Price[len(Price)-k-1])




    ChineseFont1 = FontProperties(fname = 'C:\\Windows\\Fonts\\simsun.ttc')
    plt.plot(Date_reverse,Price_reverse,"r-o",label='Price')
    plt.title("台灣加權指數",fontproperties=ChineseFont1,x=0.5,y=1.03)
    plt.xticks(fontsize=5,rotation=90)
    plt.yticks(fontsize=10)
    plt.xlabel("Date",fontsize=2,labelpad=2)
    plt.ylabel("Price",fontsize=2,labelpad=2)
    plt.legend(loc="best",fontsize=10)
    plt.tight_layout()
    plt.savefig("./picture/image_result.jpg")
    ##plt.show()