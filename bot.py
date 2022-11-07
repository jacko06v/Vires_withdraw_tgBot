
import logging

#import bot

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import pywaves
import time
import threading
import asyncio
import datetime
import csv
import tracemalloc
import pd
import os
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile
import shutil

load_dotenv()

tracemalloc.start()

#get token from .env
TOKEN = os.getenv("TOKEN")

withdrawal_block = 3372480
block = 0

admin = int(os.getenv("ADMIN_ID"))

def current_block():
    try:
        global block
        global withdrawal_block
        printInfo = 0
        while True:
            block =  pywaves.height()
            if block == withdrawal_block + 1:
                withdrawal_block = withdrawal_block + 1440
            printInfo = printInfo + 1
            if printInfo == 12:
                print("[INFO] - Current block: " + str(block))
                print("[INFO] - Block when you can withdraw your USDN: " + str(withdrawal_block))
                print("[INFO] - Blocks left: " + str(withdrawal_block - block))
                printInfo = 0
            time.sleep(5)
    except Exception as e:
        print("[ERROR] - " + str(e))
        current_block()


async def start(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " started the bot")
        with open('chat_id.csv', 'a') as f:

            writer = csv.writer(f)
            #save only if user is not already in the csv file
            if not any(str(update.message.from_user.id) in s for s in open('chat_id.csv').readlines()):
                writer.writerow([update.message.chat_id, update.message.from_user.id, update.message.from_user.username, "onlyAlert", "0", update.message.from_user.language_code])
                print("[INFO] - User " + str(update.message.from_user.id) + " added to the csv file")
        await update.message.reply_text('Hi! I will remind you how much time is left until the next withdrawal and when you can withdraw your USDN. \n\nType /help to see all the commands and /info to see info about the bot')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_minute(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every minute")
        await update.message.reply_text('Ok!\nI will notify you every minute')
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "1min"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')


async def callback_5min(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 5 minutes")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "5min"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you every 5 minutes') 
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_10min(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 10 minutes")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "10min"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you every 10 minutes')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_30min(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 30 minutes")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "30min"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you every 30 minutes')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_1hour(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every hour")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "1hour"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you every hour')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_6hour(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify every 6 hours")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "6hour"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you every 6 hours')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def callback_onlyAlert(update: Update, context):
    try:
        print("[INFO] - User " + str(update.message.from_user.id) + " set the bot to notify only when you can withdraw your USDN")
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "onlyAlert"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will notify you only when you can withdraw your USDN')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def online(update: Update, context):
    try:
        print("[INFO] - Notifying all the users that the bot is online")
        #only admin can use this command 
        if update.message.from_user.id == admin:
            with open('chat_id.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #send a message to all the users
                    await context.bot.send_message(chat_id=row[0], text="Hi! I'm online now")
        else:
            await update.message.reply_text('You are not allowed to use this command')    
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def total_users(update: Update, context):
    try:
        print("[INFO] - Notifying the total number of users")
        #only admin can use this command (admin id admin)
        if update.message.from_user.id == admin:
            with open('chat_id.csv', 'r') as f:
                reader = csv.reader(f)
                total = 0
                for row in reader:
                    total = total + 1
                await update.message.reply_text('Total users: ' + str(total))
        else:
            await update.message.reply_text('You are not allowed to use this command')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def custom_message(update: Update, context):
    try:
        #only admin can use this command (admin id admin)
        if update.message.from_user.id == admin:
            #get the message
            message = update.message.text
            #remove the command
            message = message.replace("/customMessage ", "")
            print("[INFO] - Sending custom message to all the users")
            print("[INFO] - Message: " + message)
            with open('chat_id.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #skip the first row
                    if row[0] != "chat_id":
                        #send a message to all the users
                        await context.bot.send_message(chat_id=row[0], text=message)

        else:
            await update.message.reply_text('You are not allowed to use this command')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def info(update: Update, context):
    try:
        print("[INFO] - Sending info to user " + str(update.message.from_user.id))
        await update.message.reply_text("Hi!\nI'm a bot that will notify you when you can withdraw your USDN.\n\nI'm not affiliated with the USDN or VIRES team, I'm just a bot that will notify you when you can withdraw your USDN.\n\nI'm open source, you can check the code here: https://github.com/jacko06v/Vires_withdraw_tgBot\n\nMy creator twitter: https://twitter.com/jahardyx\nand linkedIn: https://www.linkedin.com/in/jacopo-mosconi-ba5281179/")
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def get_help(update: Update, context):
    try:
        print("[INFO] - Sending help to user " + str(update.message.from_user.id))
        await update.message.reply_text("Hi!\nI'm a bot that will notify you when you can withdraw your USDN.\n\nI'm not affiliated with the USDN or VIRES team.\n\nCOMMANDS: \n\n/start - Start the bot\n/stop - Stop the bot\n/notify_1min - Be notified every minute\n/notify_5min - Be notified every 5 minutes\n/notify_10min - Be notified every 10 minutes\n/notify_30min - Be notified every 30 minutes\n/notify_1hour - Be notified every hour\n/notify_6hours - Be notified every 6 hours\n/notify_onlyAlert - Be notified only when you can withdraw your USDN\n/whenWithdraw - get info about how much time is left until next withdraw\n\n/info - Get info about the bot\n/help - Get help\n/sendFeedback - send a feedback or a comment \n\nif you want to change the time of the notification, just send the command of the time you want to be notified")
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')

async def stop(update: Update, context):
    try:
        print("[INFO] - Stopping the bot for user " + str(update.message.from_user.id))
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        #update the csv file with the new time
        with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == str(update.message.from_user.id):
                    row[3] = "stop"
                writer.writerow(row)
        shutil.move(tempfile.name, 'chat_id.csv')
        await update.message.reply_text('Ok!\nI will stop notifying you')
    except Exception as e:
        print("[ERROR] - " + str(e))
        await update.message.reply_text('An error occurred, please try again')


def start_notify():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        app = ApplicationBuilder().token(TOKEN).build()
        loop.run_until_complete(notify(app))
    except Exception as e:
        print("[ERROR] - " + str(e))
        #restart
        start_notify()
    


async def notify(app):
    try:
        print("[INFO] - Notifying all the users")
        ten_min_sent = False
        five_min_sent = False
        one_min_sent = False
        alert_sent = False
        while True:
            if withdrawal_block - block == 10 and ten_min_sent == False:
                alert_sent = False
                print("[INFO] - 10 minutes left")
                with open('chat_id.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[3] == "1min" or row[3] == "5min" or row[3] == "10min" or row[3] == "30min" or row[3] == "1hour" or row[3] == "onlyAlert":
                            await app.bot.send_message(chat_id=row[0], text="⚠️ 10 minutes to withdrawal reset! ⚠️")
                ten_min_sent = True

            elif withdrawal_block - block == 5 and five_min_sent == False:
                print("[INFO] - 5 minutes left")
                with open('chat_id.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[3] == "1min" or row[3] == "5min" or row[3] == "10min" or row[3] == "30min" or row[3] == "1hour" or row[3] == "onlyAlert":
                            await app.bot.send_message(chat_id=row[0], text="⚠️ 5 minutes to withdrawal reset! ⚠️")
                five_min_sent = True

            elif withdrawal_block - block == 1 and one_min_sent == False:
                print("[INFO] - 1 minute left")
                with open('chat_id.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[3] == "1min" or row[3] == "5min" or row[3] == "10min" or row[3] == "30min" or row[3] == "1hour" or row[3] == "onlyAlert":
                            await app.bot.send_message(chat_id=row[0], text="⚠️ 1 minute to withdrawal reset! ⚠️")
                one_min_sent = True


            elif withdrawal_block - block == 0 and alert_sent == False:
                print("[INFO] - You can withdraw your USDN")
                with open('chat_id.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[3] == "1min" or row[3] == "5min" or row[3] == "10min" or row[3] == "30min" or row[3] == "1hour" or row[3] == "onlyAlert":
                            await app.bot.send_message(chat_id=row[0], text="⚠️ YOU CAN WITHDRAW YOUR USDN! ⚠️ \n\nlet's beat the bots!")
                alert_sent = True
                ten_min_sent = False
                five_min_sent = False
                one_min_sent = False
                

            with open('chat_id.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #skip first row
                    if row[0] == "chat_id":
                        continue
                    #send a message to all the users
                    if row[3] == "1min":
                        if time.time() >= float(row[4]) + 60:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
                    elif row[3] == "5min":
                        if time.time() >= float(row[4]) + 300:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
                    elif row[3] == "10min":
                        if time.time() >= float(row[4]) + 600:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
                    elif row[3] == "30min":
                        if time.time() >= float(row[4]) + 1800:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
                    elif row[3] == "1hour":
                        if time.time() >= float(row[4]) + 3600:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
                    elif row[3] == "6hour":
                        if time.time() >= float(row[4]) + 3600*6:
                            await app.bot.send_message(chat_id=row[0], text=message())
                            chat_id = row[0]
                            #update the last time the user was notified
                            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
                            with open('chat_id.csv', 'r', newline='') as csvFile, tempfile:
                                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                                writer = csv.writer(tempfile, delimiter=',', quotechar='"')
                                for row in reader:
                                    if row[0] == chat_id:
                                        row[4] = str(time.time())
                                    writer.writerow(row)
                            shutil.move(tempfile.name, 'chat_id.csv')
    except Exception as e:
        print("[ERROR] - " + str(e))
        start_notify()

            
def message():
    try:
        remining_blocks = withdrawal_block - block
        if remining_blocks > 60:
            hours = remining_blocks // 60
            minutes = remining_blocks % 60
            time_left = str(hours) + " hours and " + str(minutes) + " minutes"
        else:
            time_left = str(remining_blocks) + " minutes"
        message="Current block: " + str(block)+"\n" + "Block when you can withdraw your USDN: " + str(withdrawal_block) + "\n" + "Blocks left: " + str(withdrawal_block - block) + "\n" + "Time left: " + time_left
        return message
    except Exception as e:
        print("[ERROR] - " + str(e))
        message()

async def adminInfo(update: Update, context):
    try:
        #only admin, print useful info
        if update.message.from_user.id == admin:
            await update.message.reply_text("Current block: " + str(block)+"\n" + "Block when you can withdraw your USDN: " + str(withdrawal_block) + "\n" + "Blocks left: " + str(withdrawal_block - block) + "\n" + "Time left: " + str((withdrawal_block - block) * 3) + " minutes")
            #users info
            with open('chat_id.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #skip first row
                    if row[0] == "chat_id":
                        continue
                    #convert last time to human readable
                    last_time = datetime.datetime.fromtimestamp(float(row[4])).strftime('%Y-%m-%d %H:%M:%S')
                    await update.message.reply_text("User: " + row[2] + "\n" + "Chat id: " + row[0] + "\n" + "Notification every: " + row[3] + "\n" + "Last notification: " + last_time)
        else:
            await update.message.reply_text("You are not admin")
    except Exception as e:
        print("[ERROR] - " + e)
        #send message 
        await update.message.reply_text("Something went wrong, please try again")

async def send_feedback(update: Update, context):
    try:
        #create a csv file with feedback if not exist
        if not os.path.exists('feedback.csv'):
            with open('feedback.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["chat_id", "name", "feedback"])
        #check if there is a message
        message = update.message.text
        message = message[14:]

        if message == "":
            await update.message.reply_text("Please add a message after /sendFeedback")
            return
        #save feedback
        with open('feedback.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([update.message.from_user.id, update.message.from_user.first_name, message])
        await update.message.reply_text("Thank you for your feedback")
    except Exception as e:
        print("[ERROR] - " + e)
        #send message 
        await update.message.reply_text("Something went wrong, please try again")

async def show_feedback(update: Update, context):
    try:
        #only admin, print feedback
        print(update.message.from_user.id)
        print(admin)
        if update.message.from_user.id == admin:
            with open('feedback.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #skip first row
                    if row[0] == "chat_id":
                        continue
                    await update.message.reply_text("User: " + row[1] + "\n" + "Chat id: " + row[0] + "\n" + "Feedback: " + row[2])
        else:
            await update.message.reply_text("You are not admin")
    except Exception as e:
        print("[ERROR] - " + e)
        #send message 
        await update.message.reply_text("Something went wrong, please try again")

async def when_withdraw(update: Update, context):
    try:
        #print when you can withdraw
        await update.message.reply_text(message())
    except Exception as e:
        print("[ERROR] - " + e)
        #send message 
        await update.message.reply_text("Something went wrong, please try again")

def main():
    print("[INFO] - Starting the bot")
    #create the chat_id.csv if it doesn't exist
    if not os.path.exists('chat_id.csv'):
        with open('chat_id.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['chat_id', 'user_id', 'username', 'time', 'lastNotify', 'len'])

    t = threading.Thread(target=current_block)
    t.start()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    t2 = threading.Thread(target=start_notify)
    t2.start()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', get_help))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('whenWithdraw', when_withdraw))
    app.add_handler(CommandHandler('notify_1min', callback_minute))
    app.add_handler(CommandHandler('notify_5min', callback_5min))
    app.add_handler(CommandHandler('notify_10min', callback_10min))
    app.add_handler(CommandHandler('notify_30min', callback_30min))
    app.add_handler(CommandHandler('notify_1hour', callback_1hour))
    app.add_handler(CommandHandler('notify_6hours', callback_6hour))
    app.add_handler(CommandHandler('notify_onlyAlert', callback_onlyAlert))
    app.add_handler(CommandHandler('online', online))
    app.add_handler(CommandHandler('totalUsers', total_users))
    app.add_handler(CommandHandler('customMessage', custom_message))
    app.add_handler(CommandHandler('adminInfo', adminInfo))
    app.add_handler(CommandHandler('stop', stop))
    app.add_handler(CommandHandler('sendFeedback', send_feedback))
    app.add_handler(CommandHandler('showFeedback', show_feedback))




    print("[INFO] - Bot started")
    app.run_polling()
  


if __name__ == '__main__':
    main()
    