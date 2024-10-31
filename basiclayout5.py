# Grid layout adalah widget yang diatur dalam kotak yang ditentukan oleh baris dan kolom.
import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        playout = PageLayout()

        btn1 = Button(text='MyButton1')
        btn2 = Button(text='MyButton2')
        btn3 = Button(text='MyButton3')

        playout.add_widget(btn1)
        playout.add_widget(btn2)
        playout.add_widget(btn3)
        # ketika dijalankan diswipe untuk melihat tampilan yang lebih jelas

        return playout


MyApp().run()
