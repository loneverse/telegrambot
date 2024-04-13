from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import smtplib
import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram Bot API token
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Replace with the target group/channel ID
TARGET_CHAT_ID = os.environ.get('TARGET_CHAT_ID')

# Email credentials
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')


def send_email(message_text):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        subject = 'New message from Telegram group'
        body = f'A new message was received: {message_text}'
        msg = f'Subject: {subject}\n\n{body}'

        server.sendmail(EMAIL_USER, 'Ayubngash7@gmail.com',
                        msg)  # Recipient email here
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()


# Function to handle incoming messages


def handle_message(update, context):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    # Check if the message is from the target chat
    if chat_id == TARGET_CHAT_ID:
        # Process the message and save it to the database
        print(f'Received message from target chat: {text}')

        # Send an email notification
        send_email(text)

        # Download any attached images and save them on local storage
        if message.photo:
            photo = message.photo[-1]  # Get the highest resolution photo
            file_id = photo.file_id
            photo_file = context.bot.get_file(file_id)
            photo_file.download(f'images/{file_id}.jpg')
            print(f'Downloaded image: images/{file_id}.jpg')

    else:
        print(f'Received message from non-target chat: {text}')


# Set up the Telegram bot
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Set up handlers
dispatcher.add_handler(MessageHandler(
    Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
print('Telegram bot is running...')
