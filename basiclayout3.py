# Grid layout adalah widget yang diatur dalam kotak yang ditentukan oleh baris dan kolom.
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class AnchourLayoutExample(GridLayout):
    def __init__(self):
        super().__init__()
        # cols, rows
        self.cols = 3
        # self.rows = 3
        self.btn = Button(text='MyButton1', size_hint=(0.2, 0.2))
        self.btn2 = Button(text='MyButton2', size_hint=(0.2, 0.2))
        self.btn3 = Button(text='MyButton3', size_hint=(0.2, 0.2))
        self.btn4 = Button(text='MyButton4', size_hint=(0.2, 0.2))
        self.btn5 = Button(text='MyButton5', size_hint=(0.2, 0.2))
        self.btn6 = Button(text='MyButton6', size_hint=(0.2, 0.2))
        self.btn7 = Button(text='MyButton7', size_hint=(0.2, 0.2))
        self.btn8 = Button(text='MyButton8', size_hint=(0.2, 0.2))
        self.btn9 = Button(text='MyButton9', size_hint=(0.2, 0.2))
        self.add_widget(self.btn)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)
        self.add_widget(self.btn7)
        self.add_widget(self.btn8)
        self.add_widget(self.btn9)


class MyApp(App):
    def build(self):

        return AnchourLayoutExample()


MyApp().run()
