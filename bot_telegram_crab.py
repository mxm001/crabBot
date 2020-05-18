from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv

def perro(bot, update):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def atr(bot, update):
    contents ="https://www.youtube.com/watch?v=v0DYwUaEIq8"

    update.message.reply_text(contents)


def gato(bot, update):
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['file']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    #comentario para que corra deploy
def chatid(bot, update):
    chat_id = update.message.chat_id
    print(str(chat_id))
def bienvenido(bot,update):
    stringBienvenida="""Bienvenido, Este es el grupo crab (cangrejos en ingles) y aca hacemos consultas, pasamos info, noticias, cosas copadas, pero siempre referido a IT... Para hablar al pedo tenemos otro grupo que es Dutty, y el enlace para unirse https://t.me/joinchat/GSa671DKtXLJrq6bxwInKg 
Y ademas de eso, tenemos una cuenta Drive Premium de google donde tenemos apuntes y cursos (+200gb.), El enlace esta en la descripcion de este grupo... Solo hay 3 reglas principales
1.- Nada de politica, religion o futbol.
2.- Nada de chistes sexistas, porque hay pocas mujeres pero las hay.
3.- No nos atacamos entre nosotros.

Despues de eso, cosas implicitas, no pregunten como hackear facebook, twiter, instagram o cualquier otra red social, porque los vamos a bannear del grupo, ademas del bulling hasta la expulsion...
Y eso es todo... 
Lo unico que quedaria, son unas preguntas obligatorias para elaborar perfiles psicologicas.

1.- windows o linux
2.- sysadmin o dev
3.- horda o alianza
4.- arco y flecha, machete o hacha.
5.- apocalipsis zombie o invasion alien.
6.- flan mixto o budin de pan
7.- juky o dadalt"""
    update.message.reply_text(stringBienvenida)  

def handle_message(bot, update):
    text = update.message.text
    if text.upper() == 'hello'.upper():
        update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
def hola(bot, update):
    update.message.reply_text('Hola {}'.format(update.message.from_user.first_name))

def cumbia(bot, update):
     update.message.reply_text('Atr perro cumbia cajeteala piola gato')

def rock(bot, update):
     update.message.reply_text('Rock and roll ah na na na')

# def simon_dice(bot, update, args):
#     user_says = " ".join(args)
#     #print(user_says)
#     if(user_says=="liven es puto?"):
#           update.message.reply_text("La verdad tenes razón")
#     else:
#           update.message.reply_text("Simon dice: " + user_says)
# def simon_pregunta(bot, update, args):
#      user_says = " ".join(args)
#      patron=r"(\S*)( es puto\?)"
#      if(re.search(patron,user_says) ):
#           update.message.reply_text("Sí, "+re.search(patron,user_says)[1]+" tiene pinta que ataja pedazos con la cola" )
#      else:
#           update.message.reply_text("Pregunta otra cosa, careta")

# def bitcoin(bot, update):
#   SECRET_KEY = os.getenv("coinmarketcap")  
#   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#     parameters = {
#       'start':'1',
#       'limit':'5000',
#       'convert':'USD'
#     }
#     headers = {
#       'Accepts': 'application/json',
#       'X-CMC_PRO_API_KEY': SECRET_KEY,
#     }
#     session = Session()
#     session.headers.update(headers)

#     try:
#       response = session.get(url, params=parameters)
#       data = json.loads(response.text)
#       print(data)
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#       print(e)
    # bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    # response = requests.get(bitcoin_api_url)
    # response_json = response.json()
    # precio_btc = float(response_json[0]['price_usd'])
    # precio_btc = round(precio_btc, 2)
    # update.message.reply_text('Precio btc: '+str(precio_btc)+" USD")



def main():
    SECRET = os.getenv("telegramext")
    updater = Updater(SECRET)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('rock',rock))
    dp.add_handler(CommandHandler('cumbia',cumbia))
    dp.add_handler(CommandHandler('chatid',chatid))
    dp.add_handler(CommandHandler('hola',hola))
    dp.add_handler(CommandHandler('bienvenido',bienvenido))
    # dp.add_handler(CommandHandler('moxi',moxi))
    # dp.add_handler(CommandHandler('btc', bitcoin))
    dp.add_handler(CommandHandler('perro',perro))
    dp.add_handler(CommandHandler('gato',gato))
    dp.add_handler(CommandHandler('atr',atr))
    # dp.add_handler(CommandHandler("simon_dice", simon_dice, pass_args=True))
    # dp.add_handler(CommandHandler("simon_pregunta", simon_pregunta, pass_args=True))
    dp.add_handler(MessageHandler(filters=Filters.text, callback=handle_message))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    load_dotenv()
    main()
