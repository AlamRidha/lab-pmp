# Grid layout adalah widget yang diatur dalam kotak yang ditentukan oleh baris dan kolom.
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        flayout = FloatLayout()
        # untuk penggunaan flayout ada beberapa yang harus dilakukan
        # pos, pos_hint, size_hint
        # pos_hint = x, y, left, right, top, bottom

        btn1 = Button(text='MyButton1', size_hint=(0.2, 0.2))
        btn1.pos_hint = {'x': 0.4, 'y': 0.4}
        # btn1.pos_hint = {'x': 0.4, 'top': 0.9}
        # btn1.pos = (200, 200)  # posisi fix, kurang responsive

        flayout.add_widget(btn1)

        return flayout


MyApp().run()
