# Grid layout adalah widget yang diatur dalam kotak yang ditentukan oleh baris dan kolom.
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        flayout = FloatLayout()

        # memberikan warna background pada window
        # jika ingin memberikan warna tapi tidak bisa dengan warna yang diinginkan tambahkan /255 dibelakangnya
        # Window.clearcolor = (252/255, 69/255, 69/255)
        # ada solusi menggunakan get color from hex
        Window.clearcolor = get_color_from_hex('#343131')

        btn1 = Button(text='MyButton1', size_hint=(0.2, 0.2))
        btn1.pos_hint = {'x': 0.4, 'y': 0.4}
        # memberikan warna background pada button
        btn1.background_color = (0, 1, 0,)

        flayout.add_widget(btn1)

        return flayout


MyApp().run()
