from pynput.keyboard import Key, Controller

def pressQToStop():
    keyboard = Controller()
    key="q"
    keyboard.press(key)
    keyboard.release(key)