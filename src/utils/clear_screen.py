# src/utilis/clear_screen.py

import os

def clear_screen():
    """Clear the terminal screen, regardless of the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')
