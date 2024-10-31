# Grid layout adalah widget yang diatur dalam kotak yang ditentukan oleh baris dan kolom.
import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        slayout = StackLayout()
        slayout.orientation = "rl-tb"
        # lr bt
        btn1 = Button(text='MyButton1', size_hint=(0.2, 0.2))
        btn2 = Button(text='MyButton2', size_hint=(0.2, 0.2))
        btn3 = Button(text='MyButton3', size_hint=(0.2, 0.2))
        btn4 = Button(text='MyButton4', size_hint=(0.2, 0.2))
        btn5 = Button(text='MyButton5', size_hint=(0.5, 0.2))
        slayout.add_widget(btn1)
        slayout.add_widget(btn2)
        slayout.add_widget(btn3)
        slayout.add_widget(btn4)
        slayout.add_widget(btn5)

        return slayout


MyApp().run()
