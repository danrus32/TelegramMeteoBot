#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telebot import types
import config
import datetime
import telebot
import random
import requests
import time
import re
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def    send_welcome(message):
    with open('data.txt', 'a') as inFile:
        line = "User logs : \n"
        line1 = "    User name: \n"+str(message.from_user.first_name)


        line2  = "\n     Time: \n"+str(datetime.datetime.today())

        line3 = "\n    Messages text : \n" + str(message.text)
        line4 = "\n    date : " + str(message)+"\n"
        print(line)
        print(line)
        print(line)
        print(line)
        inFile.write (line)
        inFile.write (line1)
        inFile.write (line2)
        inFile.write (line3)
        inFile.write (line4)
        inFile.close()

    print(message)
    print(str(message.text))
    print(message.from_user.first_name)
    markup= types.ReplyKeyboardMarkup()
    markup.row('Random')
    markup.row('')
    bot.send_message(message.chat.id ,"Привет "+ str(message.from_user.first_name)+" 😎🖐 \nВот что я могу: Для рандома нажми на 'Random\n🎲'\n Для погоды напиши 'Pogoda и город' \nПример 'Pogoda Soroca'", reply_markup=markup)

@bot.message_handler(regexp='Random')
def random_func(message):
    with open('data.txt', 'a') as inFile:
        line = "User logs : \n"
        line1 = "    User name: \n"+str(message.from_user.first_name)


        line2  = "\n     Time: \n"+str(datetime.datetime.today())
        line3 = "\n    Messages text : \n" + str(message.text)
        line4 = "\n    date : " + str(message)+"\n"
        print(line)
        print(line)
        print(line)
        print(line)
        inFile.write (line)
        inFile.write (line1)
        inFile.write (line2)
        inFile.write (line3)
        inFile.write (line4)
        inFile.close()
    markup= types.ReplyKeyboardMarkup()
    markup.row('/start')
    bot.send_message(message.chat.id,"Random number = "+ str(config.random_num()) +"\n\start", reply_markup=markup)

@bot.message_handler(regexp="Pogoda")
def handle_message(message):
    with open('data.txt', 'a') as inFile:
        line = "User logs : \n"
        line1 = "    User name: \n"+str(message.from_user.first_name)


        line2  = "\n     Time: \n"+str(datetime.datetime.today())
        line3 = "\n    Messages text : \n" + str(message.text)
        line4 = "\n    date : " + str(message)+"\n"
        print(line)
        print(line)
        print(line)
        print(line)
        inFile.write (line)
        inFile.write (line1)
        inFile.write (line2)
        inFile.write (line3)
        inFile.write (line4)
        inFile.close()
    try:
        markup= types.ReplyKeyboardMarkup()
        markup.row('/start')
        tt = re.sub("Pogoda", "",message.text)
        #for _ in range (20):
           # print(tt)
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params = {'q': tt, 'units': 'metric','lang':'ru','APPID':"b9930bca4efd191aba542903b134e0aa"})
        data = res.json()
        #print(data)
        gg = "В городе" + tt + "\nCейчас температура:\nСредняя:" + str(data['main']['temp']) +"\nMин:" + str(data['main']['temp_min']) +"\nМах"+str(data['main']['temp_min']) + "\nВлажность:" + str(data['main']['humidity'])+"\nВетер:" + str(data['wind']['speed'])+"\n"+data['weather'][0]['description']
        if data['main']['temp'] <= 5:
            bot.send_message(message.chat.id,'На улице холодно оденитесь теплее!')
        elif data['main']['temp'] >= 5:
            bot.send_message(message.chat.id,'На улице нормально!')
        elif data['main']['temp'] >= 28:
            bot.send_message(message.chat.id,'На улице горечо!')
        #print (data)
        bot.send_message(message.chat.id,gg ,reply_markup=markup)

        return(gg)
    except KeyError:
        bot.send_message(message.chat.id,"Город\страна неопознаны!", reply_markup=markup)













#if __name__ == '__main__':
bot.polling(none_stop=True)
print(message)