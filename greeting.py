import time
import pyfiglet

def get_greeting():
    current_hour = time.localtime().tm_hour

    if current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def display_greeting():
    greeting = get_greeting()
    ascii_art = pyfiglet.figlet_format(greeting)
    print(ascii_art)

if __name__ == "__main__":
    display_greeting()