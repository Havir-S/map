# STOP PROGRAM key event
import sys

def on_key_event(event):
    if event.name == 'backspace':
        sys.exit()