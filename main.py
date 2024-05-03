from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import commands as c


TOKEN: Final= "7020917378:AAGJ_A94AHiMFdzRCcR_QdoOmkDp2AZqIz8"
BOT_USERNAME: Final= "thehabercibot"


def main():

    print("Starting bot...")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", c.hello))
    app.add_handler(CommandHandler("help", c.help))
    app.add_handler(CommandHandler("news", c.get_news))
    app.add_handler(MessageHandler(filters.TEXT, c.error))
    
    

    print("Polling bot...")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()