import requests
import telebot
import time

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.from_user.username + ':' + message.text)
    bot.send_message(message.chat.id, '大家好，我是机器人')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    print(message.from_user.username + ':' + message.text)
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='有什么可以帮您')


@bot.message_handler()
def echo(message):
    # print(message.from_user.username + ':' + message.text)
    text = get_tuling_response(message.from_user.username, message.text)
    text = text.replace('{br}', '\n')

    bot.reply_to(message, text)


def get_tuling_response(userid, _info):
    # print(_info)

    api_url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + _info

    # 发送数据到执行网址
    res = requests.post(api_url, {}).json()
    # print(res, type(res))
    # 给用户返回数据
    # print(res['content'])
    return res['content']


def run():
    try:
        bot.polling()
    except BaseException:
        time.sleep(5)
        run()


if __name__ == '__main__':
    run()
