from pynput.keyboard import Controller

keyboard = Controller()
key = "q"
keyboard.press(key)
keyboard.release(key)
