from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final
from bs4 import BeautifulSoup
import requests
BOT_USERNAME: Final= "thehabercibot"
LINK = "https://www.haberler.com/son-dakika/"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} I am {BOT_USERNAME}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello! I am {BOT_USERNAME}. Please type somethiing so I can respond you.")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Command does not exist. You can use /start and /help commands.")


async def get_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.get(LINK)
    soup = BeautifulSoup(r.content, "lxml")

    news = soup.find_all('div', {'class': 'hblnBox'})
    for new in news[:5]:
        time = new.find('div', attrs={'class': 'hblnTime'}).text
        title = new.find('a').get('title')
        link = new.find('a').get('href')
        link2 = "https://www.haberler.com" + link
   
        
        my_news = "Time  : {}\nTitle : {}\nLink : {}".format(time, title, link2)
        await update.message.reply_text(my_news)
