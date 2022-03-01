from PIL import Image

def image_merge():

    image1=Image.open("./picture/result.jpg")
    image2=Image.open("./picture/result2.jpg")


    image1=image1.resize((640,480))
    image1_size=image1.size
    image2_size=image2.size



    new_image=Image.new('RGB',(image1_size[0],2*image2_size[1]))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(0,image1_size[1]))
    new_image.save("picture/image_result.jpg","JPEG")
    ##new_image.show()
image_merge()