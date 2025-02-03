# 🕵️‍♂️ Python Keylogger Project 🔐📝🔍

## 📢 Overview

The **Python Keylogger** project is a simple yet powerful tool designed to monitor and log keystrokes on a computer. It is primarily used for security and surveillance purposes, allowing users to track keyboard activity discreetly.

>[!IMPORTANT]  
> **Please note:** This tool should only be used for ethical purposes, with proper consent and authorization.

---

## 🔧 How it Works

### Initialization

The keylogger is initialized with several parameters:
- `time_interval`: The interval at which the keylogger checks for keystrokes.
- `nsfw_words_file`: The file location containing NSFW (Not Safe For Work) words for filtering.
- `bot_token`: The Telegram bot token for sending alert messages.
- `mailtrap_username` and `mailtrap_password`: Credentials for the Mailtrap SMTP server for sending email alerts.

---

### 🖋️ Keystroke Logging

- The keylogger utilizes the `pynput` library to monitor keyboard events in real-time.
- It captures keystrokes and appends them to a log string.
- The log string is continuously updated as new keystrokes are detected.

>[!CAUTION]  
> **Warning:** Ensure the keylogger is used responsibly and with the necessary permissions, as it tracks user inputs.

---

### 🚫 NSFW Filtering

- The keylogger checks the log for NSFW content by comparing it against a list of NSFW words loaded from a file.
- If any NSFW word is found in the log, an alert message is sent via Telegram and Mailtrap.
- The log is cleared after detecting NSFW content to prevent further logging of sensitive information.

---

### 📲 Alert Messaging

- The keylogger sends alert messages via Telegram and Mailtrap when NSFW content is detected.
- The Telegram bot is used to send messages to a specified chat ID.
- Mailtrap is used to send email messages to a designated recipient.

---

### 📝 Reporting

- The keylogger periodically prints the current log contents.
- This allows users to monitor keyboard activity in real-time.
- The log is cleared after printing to prevent duplication of data.

---

### 🚪 Program Termination

- The keylogger can be terminated by pressing the Enter key.
- Upon termination, the program exits gracefully, ending all threads and closing resources.

>[!TIP]  
> For a smooth exit, make sure to press the Enter key when you're ready to stop the keylogger.

---

## 🚀 Usage

1. Clone the repository and install dependencies.
2. Configure the keylogger with the required parameters.
3. Run the keylogger script.
4. Monitor keyboard activity and receive alerts for NSFW content.

> **Pro Tip:** If you are testing, ensure you’re in a safe environment before running the keylogger to avoid any unwanted logging.

---

## 🧰 Dependencies

- `pynput`: Python library for monitoring and controlling input devices.
- `python-telegram-bot`: Python wrapper for the Telegram Bot API.

---

## 📌 Contributing

Spotted a bug? Got an idea? PRs are always welcome! 🚀

📧 **Contact:** Feel free to reach out on [GitHub](https://github.com/Yuslash) for collaborations or to just say hi! 👋

>[!CAUTION]  
> **Important:** Please make sure you have explicit consent before using the keylogger in any environment.

---

## 📜 License

This project is open-source under the **MIT License**. Use it, modify it, and go crazy with it! Just don’t blame me if you get addicted to Python. 😆
