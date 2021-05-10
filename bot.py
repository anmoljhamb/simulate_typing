import telebot
from functools import partial
from secret import TOKEN
from writer import Writer

class Bot:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = telebot.TeleBot(TOKEN)
        self.LIST = []

        self.command_handler = {
            'start': self.send_welcome,
            'help': self.send_help,
            'typingList': self.typing_list,
            'clearList': self.clear_list,
            'type': self.type_number
        }

        @self.bot.message_handler(commands=self.command_handler.keys())
        def handle_commands(message):
            #Doing this because I didn't wanna manually add
            #the decorator on each command handler indivually.
            #Doing this would help the code in future, in case I wanna add
            #more commands.
            command = message.text.split()[0].lstrip('/')
            self.command_handler[command](message)

        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message):
            self.LIST.append(message)
            self.bot.reply_to(message, f"Adding this message to list. Message's Index: {len(self.LIST)-1}")

    def send_welcome(self, message):
        WELCOME_STRING = """
        I am a simple bot, made to type things out, where copy and paste is not allowed.
        """
        self.bot.reply_to(message, WELCOME_STRING)

    def send_help(self, message):
        help_string = """
        /help: for this message
        /typingList: to get all the items in list
        /type NUMBER: type the particular element from the list
        /clearList: clears the list 
        Any message sent otherwise would be added to the list
        """
        self.bot.reply_to(message, help_string)

    def clear_list(self, message):
        self.LIST.clear()
        self.bot.reply_to(message, "Clearing the list.")

    def type_number(self, message):
        text = message.text
        text = text.lstrip("/type").strip()
        try:
            list_id = int(text)
            self.bot.reply_to(self.LIST[list_id], "Typing this message.")
            self.handle_message_to_copy(self.LIST[list_id].text)
            self.bot.reply_to(message, "Done typing the message.")
        except Exception as e:
            if len(self.LIST):
                self.bot.reply_to(message, f"Some error occured. Make sure the number after /type is in the range 0 to {len(self.LIST)-1}")
                print(e)
            else:
                self.bot.reply_to(message, "Your typing list is empty. Type /help to get more information.")

    def typing_list(self, message):
        if len(self.LIST):
            TYPING_LIST = ""
            for i in range(len(self.LIST)):
                TYPING_LIST += f'{i}: {self.LIST[i].text}\n'
            self.bot.reply_to(message, TYPING_LIST)
        else:
            self.bot.reply_to(message, "The current typing list is empty.")

    
    def handle_message_to_copy(self, message):
        #Here, the given message is a string, and not the message object.
        print(message)
        #Writing the code
        writer = Writer()
        writer.write_message(message)

    def start(self):
        print("Starting the bot")
        self.bot.polling()

def main():
    bot = Bot()
    bot.start()

if __name__ == "__main__":
    main()