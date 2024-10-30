import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class AnchourLayoutExample(AnchorLayout):
    def __init__(self):
        super().__init__()
        # anchor x = left, center, right
        # anchor y = top, center, bottom
        self.anchor_x = "right"
        self.anchor_y = "top"
        self.btn = Button(text='MyButton')
        self.btn.size_hint = (0.2, 0.2)
        self.add_widget(self.btn)


class MyApp(App):
    def build(self):

        return AnchourLayoutExample()


MyApp().run()
