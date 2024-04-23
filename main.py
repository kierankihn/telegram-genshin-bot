import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    start 命令
    '''
    message = await context.bot.send_message(chat_id = update.effective_chat.id, text = '玩原神玩的', reply_to_message_id = update.effective_message.id)
    await asyncio.sleep(3)
    await context.bot.delete_messages(chat_id = update.effective_chat.id, message_ids = [message.id, update.effective_message.id])



async def ziii(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    ziii 命令
    '''
    message = await context.bot.send_message(chat_id = update.effective_chat.id, text = '⚡', reply_to_message_id = update.effective_message.id)
    await asyncio.sleep(3)
    await context.bot.delete_messages(chat_id = update.effective_chat.id, message_ids = [message.id, update.effective_message.id])

async def ganga(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    给你回复 😅
    '''
    message = await context.bot.send_message(chat_id = update.effective_chat.id, text = '😅', reply_to_message_id = update.effective_message.id)
    await asyncio.sleep(3)
    await context.bot.delete_message(chat_id = update.effective_chat.id, message_id = message.id)



# 构建 bot
API_KEY = os.getenv('TELEGRAM_API_KEY')
application = ApplicationBuilder().token(API_KEY).build()

# 注册 handler
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('ziii', ziii))
application.add_handler(MessageHandler(filters = filters.Regex('原[\s\S]*神'), callback = ganga))

# run!
application.run_polling()