import pyowm
import telebot

# от блокировок
# from telebot import apihelper
# apihelper.proxy = {'https':'socks5://127.0.0.1:9050'}

owm = pyowm.OWM('84fde4755cd373475610f37a78a25d2f', language='ru')

bot = telebot.TeleBot('1359818348:AAG5pHH2ljqX5Vv2v49lIAUrHB_9nhCSNF0')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']

        ans = f"В городе {message.text} сейчас {w.get_detailed_status()} \n"
        ans += f"Температура в районе {round(temp)} градусов"

        # if temp < 10:
        #     ans += 'Очень холодно, оденься потеплее))'
        # elif temp < 17:
        #     ans += 'Прохладно, лучше оденься:)'
        # else:
        #     ans += 'Не холодно, хоть в трусах иди:)'

        bot.send_message(message.chat.id, ans)
    except pyowm.exceptions.api_response_error.NotFoundError:
        bot.send_message(message.chat.id, 'Город не найден :(')


bot.polling(none_stop=True)
