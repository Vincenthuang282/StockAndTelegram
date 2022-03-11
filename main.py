import response as R
from telegram.ext import *



def telegram_bot():
    print("Bot Start...")
    ## Updater----->> token  ##
    ## This Class ,Which employs the telegram.ext.dispacther , provides a frontend to telegram.Bot to the programmer .... ##
    ## Its propose is to recieve the updates from Telegram and to deliver them to the dispatcher.... ##
    ## The updatercan be started as a polling service or , for production  ##
    updater = Updater("5017912090:AAEMss5Y3TOOpAOwS1J6RQkcNTIQGX0i3CU" , use_context=True)
    ## Dispacther ##
    ## This class dispatches all updates to its registered handler ##
    dp = updater.dispatcher
    ## I use two differnt handler --->>> 1. handle command 2. handle message ##
    ## CommandHandler( commands , callback) ##
    ## command--> the command or list of commands this handler should listen for .##
    ## callback--> the callback function for this handler. ##
    dp.add_handler(CommandHandler("start",R.start_command))
    dp.add_handler(CommandHandler("help",R.help_command))
    dp.add_handler(CommandHandler("Stock",R.Stock_command))
    dp.add_handler(CommandHandler("Picture",R.picture_command))
    
    dp.add_handler(CallbackQueryHandler(R.c_back_respons))
    ## MessageHandler ( filter, callback  ) ##
    ## Handler class to handle telegram messages including text,media or status updates ##
    dp.add_handler(MessageHandler(Filters.text,R.handle_message))
    dp.add_handler(MessageHandler(Filters.location,R.handle_location))
    
    
    ## Start polling Update from Telegram ##
    updater.start_polling(drop_pending_updates=True)
telegram_bot()
##
##telegram_token=key.API_KEY
##print(telegram_token)
##telegram_chat_id='-602160137'
##print(telegram_chat_id)
##
##photo_path='picture\pic01.jpg'
##bot=telegram.Bot(token=telegram_token)
##bot.send_message(chat_id=telegram_chat_id,text='From Telegram Bot')
##bot.send_photo(chat_id=telegram_chat_id,photo=open(photo_path,'rb'))
##
