from datetime import datetime
from weather import weather
from geopy.geocoders import Nominatim
from stock import stock
from telegram import InlineKeyboardMarkup , InlineKeyboardButton
import telegram
from picturemaker_1 import PictureMaker
from picturemaker_2 import PictureMaker2
from picture_merge import image_merge

def start_command(update , context):
    update.message.reply_text('Type Something Random to get started it !')
    
def help_command(update , context):
    with open("help.txt","r",encoding='utf-8') as file:
        list=file.read()
        update.message.reply_text(list)

def handle_message(update, context):
    text=str(update.message.text).lower()
    user_message = str(text).lower()
    print(update['message']['text'])

    if user_message in ('hello','hi','sup'):
        response="Hey How's Going"
    elif user_message in ('who are you','who are you?'):
        response="I am Vincent's bot!"
    elif user_message in ('time','time?'):
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
        response=str(date_time)
    else:
        response="I don't know"
    update.message.reply_text(response) 
def picture_command(update,context):
    input_arr=[]
    arr=str(update['message']['text']).split()
    for i in range( 1 , len(arr) , 1):
        input_arr.append(arr[i])
    string=" "
    for i in range(0,len(input_arr),1):
        string+=input_arr[i]+" "
    update.message.reply_text('Choose the days u wanna show in'+string ,reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='30days',callback_data='30')],
        [InlineKeyboardButton(text='45days',callback_data='45')],
        [InlineKeyboardButton(text='60days',callback_data='60')]
    ]))
    
    ##print(telegram_token)
    telegram_chat_id=update['message']['chat']['id']
    print(telegram_chat_id)
    
    #PictureMaker(input_arr,day)
    #PictureMaker2(day)
    #image_merge()
    #photo_path='picture/image_result.jpg'
    #bot=telegram.Bot(token=telegram_token)
    #bot.send_photo(chat_id=telegram_chat_id,photo=open(photo_path,'rb'))

def c_back_respons(update,context):
    input_arr=[]
    days=str(update.callback_query.data)
    
    arr=str(update.callback_query.message.text[32:]).split()
    for i in range(0,len(arr),1):
        input_arr.append(arr[i])
    telegram_token="5017912090:AAEMss5Y3TOOpAOwS1J6RQkcNTIQGX0i3CU"
    telegram_chat_id=update.callback_query.message.chat.id
    PictureMaker(input_arr,days)
    PictureMaker2(days)
    image_merge()
    photo_path='picture/image_result.jpg'
    bot=telegram.Bot(token=telegram_token)
    bot.send_photo(chat_id=telegram_chat_id,photo=open(photo_path,'rb'))
    


def Stock_command(update , context):
        print(update)
        stock_num=update['message']['text'][6:]
        stock_num=str(stock_num).lstrip()
        if (stock_num.isspace())|(stock_num == ""):
            update.message.reply_text("Enter The Correct Number Such As  ------>   /stock TSLA")
        else :
            news=stock(stock_num)
            update.message.reply_text(stock_num+' Latest Six News ',
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text=news[0]['title'],url=news[0]['url']),],
                    [InlineKeyboardButton(text=news[1]['title'],url=news[1]['url']),],
                    [InlineKeyboardButton(text=news[2]['title'],url=news[2]['url']),],
                    [InlineKeyboardButton(text=news[3]['title'],url=news[3]['url']),],
                    [InlineKeyboardButton(text=news[4]['title'],url=news[4]['url']),],
                    [InlineKeyboardButton(text=news[5]['title'],url=news[5]['url']),],
                                       ] ))
    
        

def handle_location(update,context):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Assign Latitude & Longitude
    Latitude=str(update['message']['location']['latitude'])
    Longitude=str(update['message']['location']['longitude'])
    # Get location with geocode
    location = geolocator.geocode(Latitude+","+Longitude)
    #change it to the string
    location=str(location)
    # save the location as array
    location=location.split(', ')
    list=''.join(['臺','灣','省'])
    city=location[len(location)-3]
    if city == list :
        city=location[len(location)-4]
    city=city[0:2] 
    update.message.reply_text(weather(city))
    


