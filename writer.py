from pynput.keyboard import Key, Controller
import random 
import time 

class Writer:
    def __init__(self, sleeping_time=0.02, use_tabs=False, make_mistakes=True, waiting_time=2):
        '''
        SLEEPING_TIME: The waiting time between pressing two keys. 
        USE_TABS: The code is intended to copy code from one place to another, 
        and if the user wants, he can change 4 spaces to tabs, if this function is true
        MAKE_MISTAKES: A use case for this would be if the document is a shared document
        and somebody is keeping an eye on you, so this would allow the code to make mistakes
        after every 20 to 30 letters, to not raise suspicion. 
        WAITING_TIME: The waiting time before the code starts typing.
        '''
        self.keyboard = Controller()
        self.sleeping_time = sleeping_time
        self.use_tabs = use_tabs
        self.make_mistakes = make_mistakes
        self.waiting_time = waiting_time

    def write_message(self, message):
        mistake_after = random.randint(15, 30)
        time.sleep(self.waiting_time)
        counter = 0 
        for index, letter in enumerate(message):
            if counter == mistake_after:
                counter = 0
                mistake_after = random.randint(15, 30)
                if self.make_mistakes:
                    self.make_mistake(letter)
            if letter in ['\n', '\t']:
                if letter == '\n': 
                    letter = Key.enter
                else:
                    letter = Key.tab 
                self.keyboard.press(letter)
                self.keyboard.release(letter)
            elif letter == " ":
                if not self.use_tabs:
                    self.keyboard.press(letter)
                    self.keyboard.release(letter)
                else:
                    #means we need to convert every 4 spaces to 1 tab 
                    count = 1
                    while message[index] == " ":
                        count += 1 
                        index += 1 
                    if count%4 == 0:
                        count = count // 4
                        for _ in range(count):
                            self.keyboard.press(Key.tab)
                            self.keyboard.release(Key.tab)
                            time.sleep(self.sleeping_time)
            else:
                self.keyboard.press(letter)
                self.keyboard.release(letter)
            time.sleep(self.sleeping_time)
            counter += 1 

    def make_mistake(self, curr_letter):
        '''
        To make mistakes more beliveable, the code will make
        the same mistakes a human would make, for example, 
        if a person is going to press the letter 'a' then most probably the
        person could mispress it as s instead of, or z. To make the code simpler
        I am just consdering the side letters. You can customize the code yourself
        '''
        UPPER_ROW = "QWERTYUIOP["
        MIDDLE_ROW = "ASDFGHJKL;"
        BOTTOM_ROW = "ZXCVBNM,."

        LIST = [UPPER_ROW, MIDDLE_ROW, BOTTOM_ROW]
        
        for curr_list in LIST:
            if letter.upper() in curr_list:
                curr_index = curr_list.index(letter.upper())
                original_index = curr_index 
                curr_index = curr_index + random.choice([-1, 1])

                #Making mistake
                self.keyboard.press(curr_list[curr_index])
                self.keyboard.release(curr_list[curr_index])
                time.sleep(self.sleeping_time)
                #Erasing mistake
                self.keyboard.press(Key.backspace)
                self.keyboard.release(Key.backspace)
                time.sleep(self.sleeping_time)


def main():
    writer = Writer(make_mistakes=False, waiting_time=4)
    print("Writing message")
    writer.write_message("Hello World!")

if __name__ == "__main__":
    main()