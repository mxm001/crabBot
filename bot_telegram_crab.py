from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
    
    
def perro(bot, update):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def gato(bot, update):
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def chatid(bot, update):
    chat_id = update.message.chat_id
    print(str(chat_id))
    
    
def hola(bot, update):
    update.message.reply_text('Hola {}'.format(update.message.from_user.first_name))

def moxi(bot, update):
    update.message.reply_text('Moxi es puto')

def cumbia(bot, update):
     update.message.reply_text('Atr perro cumbia cajeteala piola gato')
        
def rock(bot, update):
     update.message.reply_text('Rock and roll ah na na na')

def simon_dice(bot, update, args):
    user_says = " ".join(args)
    #print(user_says)
    if(user_says=="liven es puto?"):
          update.message.reply_text("La verdad tenes razón")
    else:
          update.message.reply_text("Simon dice: " + user_says)
def simon_pregunta(bot, update, args):
     user_says = " ".join(args)
     patron=r"(\S*)( es puto\?)"
     if(re.search(patron,user_says) ):
          update.message.reply_text("Sí, "+re.search(patron,user_says)[1]+" tiene pinta que ataja pedazos con la cola" )
     else:
          update.message.reply_text("Pregunta otra cosa, careta")

def bitcoin(bot, update):
    bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    precio_btc = float(response_json[0]['price_usd'])
    precio_btc = round(precio_btc, 2)
    update.message.reply_text('Precio btc: '+str(precio_btc)+" USD")
   
    
    
def main():
    updater = Updater('832075970:AAGuFaXyf70znt1OkhF_Od1o3-06DN7YCsE')
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('rock',rock))
    dp.add_handler(CommandHandler('cumbia',cumbia))
    dp.add_handler(CommandHandler('chatid',chatid))
    dp.add_handler(CommandHandler('hola',hola))
    dp.add_handler(CommandHandler('moxi',moxi))
    dp.add_handler(CommandHandler('btc', bitcoin))
    dp.add_handler(CommandHandler('altokperro',perro))
    dp.add_handler(CommandHandler('piolagato',gato))
    dp.add_handler(CommandHandler("simon_dice", simon_dice, pass_args=True))
    dp.add_handler(CommandHandler("simon_pregunta", simon_pregunta, pass_args=True))

    updater.start_polling()
    updater.idle()
    
    
    
if __name__ == '__main__':
    main()
