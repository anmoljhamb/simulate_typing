# Simulate Typing Bot 🤖

A Python script that uses a Telegram bot to remotely type out text or code, simulating human keystrokes. This is perfect for situations like online coding competitions or workshops where copy-pasting is disabled.

## The Problem 🤔

During a coding competition, participants had to write code in a shared Google Doc where copy-pasting from a local IDE was forbidden. Manually typing everything is slow and error-prone. This tool was built to solve that problem by automating the typing process in a human-like way.

## Features ✨

* **Remote Control:** Send text and commands from anywhere using the Telegram app.
* **Human-like Typing:** Simulates typing character by character with configurable delays.
* **Realistic Mistakes:** An optional feature to simulate common typing errors (like hitting an adjacent key) and then correcting them, making the automation less detectable.
* **Simple Command Interface:** Easily manage a queue of text snippets to be typed.
* **Cross-Platform:** Works on any OS with Python support.

## How It Works

1.  You send a message (code snippet, command, etc.) to your personal Telegram bot.
2.  A Python script running on your computer receives the message.
3.  Any plain text message is added to a typing queue.
4.  You send the `/type <index>` command to the bot.
5.  The script focuses on your active window (e.g., Google Docs, IDE) and programmatically types out the selected message using the `pynput` library.

## Setup & Installation 🚀

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/simulate-typing.git](https://github.com/your-username/simulate-typing.git)
    cd simulate-typing
    ```

2.  **Create a Telegram Bot:**
    * Talk to the [BotFather](https://t.me/botfather) on Telegram.
    * Create a new bot by sending `/newbot`.
    * BotFather will give you a unique **token**. Copy it.

3.  **Configure the Bot:**
    * Create a file named `secret.py`.
    * Add your token to it like this:
        ```python
        # secret.py
        TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
        ```

4.  **Install dependencies:**
    * It's recommended to use a virtual environment.
    * Install the required libraries from `requirements.txt`.
        ```bash
        # Create requirements.txt with the following lines:
        # pyTelegramBotAPI
        # pynput

        pip install -r requirements.txt
        ```

5.  **Run the bot:**
    ```bash
    python bot.py
    ```
    Your bot is now live!

## Usage Guide 📋

1.  Open the Telegram app and start a conversation with the bot you created.
2.  Open the application you want to type into on your computer (e.g., a text editor, Google Docs). **Make sure its window is active.**
3.  Send any text or code snippet as a message to the bot. It will be added to the typing queue.
4.  Use the commands below to manage and trigger the typing.

### Commands

| Command             | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| `/start`            | Shows a welcome message.                                                  |
| `/help`             | Displays the list of available commands.                                  |
| `/typingList`       | Shows all messages currently in the queue with their index.               |
| `/type <index>`     | Types the message at the specified index. **Example:** `/type 0`.         |
| `/clearList`        | Clears all messages from the typing queue.                                |
| `(any other text)`  | Adds the text to the typing queue.                                        |

## Configuration

You can customize the typing behavior by modifying the parameters in the `Writer` class (`writer.py`):

* `sleeping_time`: The delay (in seconds) between each keystroke.
* `make_mistakes`: Set to `True` or `False` to enable/disable the realistic mistakes feature.
* `waiting_time`: The delay (in seconds) after sending the `/type` command before typing begins, giving you time to switch to the correct window.
