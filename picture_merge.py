from PIL import Image

def image_merge():

    image1=Image.open("C:/Users/VINCENT/OneDrive/桌面/StockAndTelegram/picture/result.jpg")
    image2=Image.open("C:/Users/VINCENT/OneDrive/桌面/StockAndTelegram/picture/result2.jpg")


    image1=image1.resize((640,480))
    image1_size=image1.size
    image2_size=image2.size



    new_image=Image.new('RGB',(image1_size[0],2*image2_size[1]))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(0,image1_size[1]))
    new_image.save("C:/Users/VINCENT/OneDrive/桌面/StockAndTelegram/picture/image_result.jpg","JPEG")
    ##new_image.show()
image_merge()
