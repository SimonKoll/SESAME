from pynput.keyboard import Controller


def pressQToStop():
    keyboard = Controller()
    key = "q"
    keyboard.press(key)
    keyboard.release(key)
