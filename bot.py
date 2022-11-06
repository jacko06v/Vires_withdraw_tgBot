
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Updater
import pywaves
import time
import threading
import asyncio
import datetime
import csv
import tracemalloc
import pd
import os

tracemalloc.start()

#get token from .env
TOKEN = os.getenv("TOKEN")
withdrawal_block = 3371040
block = 0


def current_block():
    global block
    global withdrawal_block
    while True:
        block =  pywaves.height()
        if block >= withdrawal_block:
            withdrawal_block = withdrawal_block + 1440
        print("[INFO] - Current block: " + str(block))
        print("[INFO] - Block when you can withdraw your USDN: " + str(withdrawal_block))
        print("[INFO] - Blocks left: " + str(withdrawal_block - block))
        time.sleep(5)


def start(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " started the bot")
    with open('chat_id.csv', 'a') as f:
        writer = csv.writer(f)
        #write chat_id, user_id, username and "onlyAlert" to the csv file
        writer.writerow([update.message.chat_id, update.message.from_user.id, update.message.from_user.username, "onlyAlert"])
    update.message.reply_text('Hi! I will notify you when you can withdraw your USDN. \nUse /1min to get notified every minute \nUse /5min to get notified every 5 minutes \nUse /10min to get notified every 10 minutes \nUse /30min to get notified every 30 minutes \nUse /1hour to get notified every hour \nUse /onlyAlert to get notified only when you can withdraw your USDN')

def callback_minute(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every minute")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "1min"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you every minute')

def callback_5min(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 5 minutes")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "5min"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you every 5 minutes') 

def callback_10min(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 10 minutes")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "10min"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you every 10 minutes')

def callback_30min(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 30 minutes")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "30min"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you every 30 minutes')

def callback_1hour(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every hour")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "1hour"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you every hour')

def callback_onlyAlert(update: Update, context):
    print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify only when you can withdraw your USDN")
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "onlyAlert"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will notify you only when you can withdraw your USDN')

def online(update: Update, context):
    print("[INFO] - Notifying all the users that the bot is online")
    #only admin can use this command (admin id 168989469)
    if update.message.from_user.id == 168989469:
        with open('chat_id.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                #send a message to all the users
                update.message.bot.send_message(chat_id=row[0], text="Hi! I'm online now")
    else:
        update.message.reply_text('You are not allowed to use this command')    

def total_users(update: Update, context):
    #pd
    print("[INFO] - Total users: " + str(len(pd.read_csv('chat_id.csv'))))
    #only admin can use this command (admin id 168989469)
    if update.message.from_user.id == 168989469:
        update.message.reply_text('Total users: ' + str(len(pd.read_csv('chat_id.csv'))))
    else:
        update.message.reply_text('You are not allowed to use this command')

def custom_message(update: Update, context):
    #only admin can use this command (admin id 168989469)
    if update.message.from_user.id == 168989469:
        #get the message
        message = update.message.text
        #remove the command
        message = message.replace("/customMessage ", "")
        print("[INFO] - Sending custom message to all the users")
        print("[INFO] - Message: " + message)
        with open('chat_id.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                #send a message to all the users
                update.message.bot.send_message(chat_id=row[0], text=message)
    else:
        update.message.reply_text('You are not allowed to use this command')

def info(update: Update, context):
    print("[INFO] - Sending info to user " + str(update.message.from_user.id))
    update.message.reply_text("Hi!\n I'm a bot that will notify you when you can withdraw your USDN.\n\nI'm not affiliated with the USDN or VIRES team, I'm just a bot that will notify you when you can withdraw your USDN.\n\nI'm open source, you can check the code here: https://github.com/jacko06v/Vires_withdraw_tgBot\n\nMy creator twitter: https://twitter.com/jahardyx and linkedIn: https://www.linkedin.com/in/jacopo-mosconi-ba5281179/")

def get_help(update: Update, context):
    print("[INFO] - Sending help to user " + str(update.message.from_user.id))
    update.message.reply_text("Hi!\nI'm a bot that will notify you when you can withdraw your USDN.\n\nI'm not affiliated with the USDN or VIRES team.\n\n COMMANDS: \n\n/start - Start the bot\n/stop - Stop the bot\n/notify_1min - Be notified every minute\n/notify_5min - Be notified every 5 minutes\n/notify_10min - Be notified every 10 minutes\n/notify_30min - Be notified every 30 minutes\n/notify_1hour - Be notified every hour\n/notify_onlyAlert - Be notified only when you can withdraw your USDN\n\n/info - Get info about the bot\n/help - Get help")

def stop(update: Update, context):
    print("[INFO] - Stopping the bot for user " + str(update.message.from_user.id))
    with open('chat_id.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == str(update.message.from_user.id):
                #update the csv file with the new time
                row[3] = "False"
                with open('chat_id.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(reader)
    update.message.reply_text('Ok!\nI will stop notifying you')

def main():
    print("[INFO] - Starting the bot")
    #create the chat_id.csv if it doesn't 




    t = threading.Thread(target=current_block)
    t.start()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', get_help))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('notify_1min', callback_minute))
    app.add_handler(CommandHandler('notify_5min', callback_5min))
    app.add_handler(CommandHandler('notify_10min', callback_10min))
    app.add_handler(CommandHandler('notify_30min', callback_30min))
    app.add_handler(CommandHandler('notify_1hour', callback_1hour))
    app.add_handler(CommandHandler('notify_onlyAlert', callback_onlyAlert))
    app.add_handler(CommandHandler('online', online))
    app.add_handler(CommandHandler('totalUsers', total_users))
    app.add_handler(CommandHandler('customMessage', custom_message))
    app.add_handler(CommandHandler('stop', stop))

    print("[INFO] - Bot started")
    app.run_polling()
  


if __name__ == '__main__':
    main()
    