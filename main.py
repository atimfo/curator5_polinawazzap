import telebot

bot = telebot.TeleBot('6435761029:AAHlthvJTfUDt-jNOJkYuypAltHHw5GTIa4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Факт номер один: В теле среднестатистического человека достаточно железа, чтобы сделать гвоздь длиной 7,62 сантиметра.\nЧтобы узнать ещё один факт, скажи Next.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['Next'])
def main(message):
    bot.send_message(message.chat.id,
                     'Факт номер два: Каждое лето Эйфелева башня становится на *15* сантиметров выше. \nЧтобы узнать следующий факт, скажи Love.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['Love'])
def main(message):
    bot.send_message(message.chat.id,
                     'Факт номер три: Новорождённый детёныш кенгуру может поместиться в чайной ложке. \nЧтобы узнать следующий факт, скажи You.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['You'])
def main(message):
    bot.send_message(message.chat.id,
                     'Факт номер четыре: Чтобы зарядить один iPhone, нужно 595 апельсинов.\nЧтобы узнать следующий факт, скажи Goodbye.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['Love'])
def main(message):
    bot.send_message(message.chat.id,
                     'Факт номер пять:[все факты взяты отсюда (https://dymontiger.livejournal.com/15806868.html?ysclid=lpinjnisbp64158154) ',
                     parse_mode='Markdown')


bot.infinity_polling()