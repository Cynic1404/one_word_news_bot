import telebot
from credentials import bot_token
from newsapi import NewsApiClient
from credentials import news_api
from telebot import types

bot = telebot.TeleBot(bot_token)
newsapi = NewsApiClient(api_key=news_api)
current_page = 1
topic = None


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.reply_to(message, "Type one word to select a topic for news")
    bot.register_next_step_handler_by_chat_id(message.chat.id, news)


def news(message):
    global topic
    topic = message
    reply = all_articles(message.text, current_page)
    markup = types.InlineKeyboardMarkup(row_width=1)
    next_5 = types.InlineKeyboardButton('next 5', callback_data='next')
    new = types.InlineKeyboardButton('new topic', callback_data='new')
    markup.add(next_5, new)
    bot.send_message(message.chat.id, " \n\n".join(reply), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(callback):
    if callback.message:
        global current_page, topic
        if callback.data == "next":
            current_page += 1
            news(topic)
        elif callback.data == "new":
            first_message(topic)


def all_articles(word, page):
    response = newsapi.get_everything(q=word,
                                      language='en',
                                      sort_by='relevancy', page_size=5,
                                      page=page)
    articles = [f"{i['title']} \n{i['url']}" for i in response['articles']]
    return articles


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
