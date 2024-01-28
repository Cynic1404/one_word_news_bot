# Telegram News Bot

#### Video Demo: [Watch Demo](https://youtu.be/4SttbEuG6Ww?si=J2r0HJeEwjXeNaK0)

## Description

This Python program serves as a Telegram bot designed to fetch and display news articles based on user-selected topics. The bot is integrated with the News API to retrieve relevant articles, allowing users to navigate through news pages and seamlessly choose new topics.

## Dependencies

- **Telebot:** A Python library for interacting with the Telegram Bot API.
- **News API:** An API for fetching news articles.

## Usage

1. Register your Telegram bot. ([Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial#getting-ready))
2. Generate an API token for [News API](https://newsapi.org/).
3. Ensure you have the required credentials for the Telegram Bot API (`bot_token`) and the News API (`news_api`) in the `credentials.py` file.
4. Run the program, and the bot will be active on Telegram.
   
**Note:** Keep your credentials secure and avoid sharing them publicly.

## How to Use

1. Start the bot by sending the '/start' command.
2. Enter a single word to choose a topic for news articles.
3. Navigate through articles using the provided options in the inline keyboard.
4. Choose a new topic or continue exploring articles.

