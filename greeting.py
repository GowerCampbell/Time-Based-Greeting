import time
import pyfiglet
from datetime import datetime
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

# Initialize the console for rich formatting
console = Console()

# Function to get greeting based on the current time
def get_greeting():
    """Returns a time-based greeting."""
    current_hour = time.localtime().tm_hour

    if current_hour < 12:
        return "Good Morning!", "yellow", "black"  # Text color: yellow, background color: black
    elif 12 <= current_hour < 18:
        return "Good Afternoon!", "blue", "white"
    else:
        return "Good Evening!", "magenta", "black"

# Function to create and display ASCII art with greeting
def display_ascii_art(greeting):
    """Generate and display the ASCII art for the greeting."""
    ascii_art = pyfiglet.figlet_format(greeting)
    return ascii_art

# Function to display the greeting, ASCII art, and time with background
def display_greeting():
    """Continuously display greeting, ASCII art, and current time with background color."""
    while True:
        # Get the greeting, text color, and background color
        greeting, text_color, bg_color = get_greeting()

        # Create ASCII art for the greeting
        ascii_art = display_ascii_art(greeting)

        # Get the current time formatted as HH:MM:SS
        current_time = datetime.now().strftime("%H:%M:%S")

        # Clear the console for the next update
        console.clear()

        # Create a Panel for background color with the greeting text
        greeting_panel = Panel(ascii_art, style=f"{text_color} on {bg_color}", expand=False)

        # Display the greeting with background and current time
        console.print(greeting_panel, justify="center")
        console.print(f"Current Time: {current_time}", style="bold white", justify="center")

        # Sleep for 1 second to update the display
        time.sleep(1)

if __name__ == "__main__":
    display_greeting()

