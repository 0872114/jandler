from pynput.keyboard import Key, Listener
from pygame import mixer
from time import time


class KeySound:

    keys_down = set()

    def __init__(self):
        mixer.init()
        mixer.set_num_channels(99)
        self.prs = mixer.Sound('media/prs.wav')
        self.rls = mixer.Sound('media/rls.wav')
        self.dng = mixer.Sound('media/dng.wav')

        mixer.music.load('media/prs.wav')

        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        free_channel = mixer.find_channel()
        free_channel.play(self.prs)
        print(1)
        return
        if key not in self.keys_down:
            self.keys_down.add(key)

            if key == Key.enter:
                self.dng.play()
            else:
                self.prs.play()

            print('{0} pressed'.format(
                key))

    def on_release(self, key):
        return
        free_channel = mixer.find_channel()
        free_channel.play(self.rls)
        return

        if key in self.keys_down:
            self.keys_down.remove(key)
        if key != Key.enter:
            self.rls.play()


        print('{0} release'.format(
            key))


keys_sound = KeySound()
