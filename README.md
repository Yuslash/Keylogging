# Python Keylogger

🔐📝🔍

## Introduction

This Python script is a simple keylogger that logs keystrokes and detects NSFW content. It sends alert messages via Telegram and Mailtrap when NSFW content is detected.

## Usage

1. Clone the repository:

git clone https://github.com/yourusername/python-keylogger.git

2. Install dependencies:


3. Provide necessary configurations:
- Provide the file location of the NSFW words dataset in `nsfw_words_file` variable.
- Replace `bot_token`, `mailtrap_username`, and `mailtrap_password` with your Telegram bot token, Mailtrap username, and password respectively.

4. Run the script:


## Dependencies

- `pynput`: Python library to monitor and control input devices.
- `python-telegram-bot`: Python wrapper for the Telegram Bot API.

## Configuration

- `nsfw_words_file`: File location of the NSFW words dataset.
- `bot_token`: Your Telegram bot token.
- `mailtrap_username`: Your Mailtrap username.
- `mailtrap_password`: Your Mailtrap password.

## Contact

For any issues or suggestions, please contact [yourusername](mailto:youremail@example.com).
