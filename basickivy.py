from kivy.app import App
from kivy.lang import Builder


class MainApp(App):
    def build(self):
        # membuka file interface.kv
        return Builder.load_file('interface.kv')


MainApp().run()
