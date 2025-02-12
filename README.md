
# Time-Based Greeting

This is a Python project that displays a time-based greeting with dynamic text and ASCII art designs. The program updates every second, showing a greeting based on the current time of day (morning, afternoon, evening), along with the current time. It also incorporates a background color for each greeting based on the time of day.

## Features

- **Dynamic Time-Based Greetings**: Displays different greetings depending on the time of day.
- **ASCII Art**: Uses the `pyfiglet` library to generate ASCII art for the greeting text.
- **Customizable Background Colors**: The greeting is displayed with different background colors for morning, afternoon, and evening.
- **Real-Time Clock**: The program updates the current time every second and displays it below the greeting.

## Code Breakdown

### 1. **Importing Libraries**

```python
import time
import pyfiglet
from datetime import datetime
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
```

- **time**: Used to handle time-related tasks (e.g., getting the current time).
- **pyfiglet**: Used to generate ASCII art from the greeting text.
- **datetime**: Used to get the current date and time.
- **rich.console**: Used for styled and colorful terminal output.
- **rich.text**: Provides `Text` objects for styled text.
- **rich.panel**: Used to create styled panels (to add background color).

### 2. **Defining the Greeting Function**

```python
def get_greeting():
    """Returns a time-based greeting."""
    current_hour = time.localtime().tm_hour

    if current_hour < 12:
        return "Good Morning!", "yellow", "black"  # Text color: yellow, background color: black
    elif 12 <= current_hour < 18:
        return "Good Afternoon!", "blue", "white"
    else:
        return "Good Evening!", "magenta", "black"
```

- The `get_greeting` function checks the current time and returns a greeting along with its text color and background color.
- **Morning (before 12)**: Yellow text with black background.
- **Afternoon (12-18)**: Blue text with white background.
- **Evening (after 18)**: Magenta text with black background.

### 3. **Generating ASCII Art**

```python
def display_ascii_art(greeting):
    """Generate and display the ASCII art for the greeting."""
    ascii_art = pyfiglet.figlet_format(greeting)
    return ascii_art
```

- This function uses the `pyfiglet` library to generate ASCII art from the provided greeting text.

### 4. **Displaying the Greeting with Background and Time**

```python
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
```

- The `display_greeting` function continuously runs and:
  1. Gets the greeting and colors from the `get_greeting` function.
  2. Generates the ASCII art for the greeting.
  3. Displays the current time.
  4. Clears the console every second and updates the display.

- **Panel with Background**: The `rich.panel.Panel` is used to create a background with the greeting, where the background color changes depending on the time of day.

### 5. **Starting the Program**

```python
if __name__ == "__main__":
    display_greeting()
```

- This section ensures the program starts by calling the `display_greeting` function when the script is executed.

## GitHub Actions Workflow

This project includes a GitHub Actions workflow to automate **testing**, **linting**, and **dependency installation**.

### Workflow Features:

- **Python Setup**: The workflow sets up Python 3.10.
- **Dependency Installation**: Installs `flake8` for linting and `pytest` for testing.
- **Linting**: Ensures code follows Python style guidelines using `flake8`.
- **Testing**: Runs tests using `pytest`.
- **Continuous Integration (CI)**: Runs the workflow whenever changes are pushed to the `main` branch or a pull request is opened.

### Workflow File (`.github/workflows/python-app.yml`):

```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Time-Based-Greeting.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Time-Based-Greeting
   ```

3. Install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python greeting.py
   ```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
