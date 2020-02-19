from pynput.keyboard import Key, Listener
from playsound import playsound


class KeySound:

    keys_down = set()

    def __init__(self):
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if key not in self.keys_down:
            self.keys_down.add(key)
            print('{0} pressed'.format(
                key))

            if key == Key.enter:
                playsound("media/dng.wav", False)
            else:
                playsound("media/prs.wav", False)

    def on_release(self, key):
        print('{0} release'.format(
            key))

        if key in self.keys_down:
            self.keys_down.remove(key)
        if key != Key.enter:
            playsound("media/rls.wav", False)


keys_sound = KeySound()
