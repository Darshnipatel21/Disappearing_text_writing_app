# Disappearing Text Writing App

A fun and engaging writing application that helps improve your writing focus by ensuring you keep writing without long pauses. If you stop typing, all your progress will be lost!

## Features

- **Disappearing Text**: If you stop typing for 10 seconds, your text will disappear.
- **Reset Button**: Manually reset the text at any time.
- **Save Button**: Save your text to a file before it disappears.


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Darshnipatel21/Disappearing_text_writing_app.git
    cd disappearing-text-writing-app
    ```

2. **Install the required dependencies**:
    Make sure you have Python installed. You can install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python disappearing_text_app.py
    ```

## Usage

- **Typing**: Start typing in the text area. The countdown timer will reset with every key press.
- **Reset**: Click the `Reset` button to clear the text manually.
- **Save**: Click the `Save` button to save your text to a file named `Last Disappeared Text.txt`.

## Code Overview

### Main Components

- **DisappearingTextWritingApp Class**: The main application class handling UI components and functionality.
- **createWidgets Method**: Sets up the UI components.
- **start_timer Method**: Starts the countdown timer.
- **on_key_press Method**: Resets the timer when a key is pressed.
- **reset_timer Method**: Cancels the current timer and starts a new one.
- **user_inactive Method**: Clears the text when the user is inactive for the set duration.
- **save_text Method**: Saves the current text to a file.

### Acknowledgements
- Python
- Tkinter

### Contact
If you have any questions or suggestions, feel free to reach out:

- **Email:** darshni211196@gmail.com
- **GitHub:** https://github.com/Darshnipatel21

