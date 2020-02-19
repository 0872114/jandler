from pynput.keyboard import Key, Listener
from pygame import mixer
from time import time


class KeySound:

    keys_down = set()

    def __init__(self):
        mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        self.prs = mixer.Sound('media/prs.wav')
        self.rls = mixer.Sound('media/rls.wav')
        self.dng = mixer.Sound('media/dng.wav')
        self.shfdn = mixer.Sound('media/shfdn.wav')
        self.shfup = mixer.Sound('media/shfup.wav')

        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if self.keys_down == {Key.delete, Key.ctrl_l}:
            exit(0)
        if key not in self.keys_down:
            self.keys_down.add(key)
            free_channel = mixer.find_channel()

            if key == Key.enter:
                free_channel.play(self.dng)
            elif key in (Key.shift, ):
                free_channel.play(self.shfup)
            elif key == Key.caps_lock:
                free_channel.play(self.shfup)
            else:
                free_channel.play(self.prs)
        elif key == Key.caps_lock:
            free_channel = mixer.find_channel()
            free_channel.play(self.shfdn)
            self.keys_down.remove(key)

    def on_release(self, key):
        if key in self.keys_down and key != Key.caps_lock:
            self.keys_down.remove(key)

        free_channel = mixer.find_channel()
        if key == Key.shift:
            free_channel.play(self.shfdn)
        elif key not in (Key.enter, Key.caps_lock):
            free_channel.play(self.rls)


keys_sound = KeySound()
