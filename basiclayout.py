import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        blyt = BoxLayout(orientation='horizontal')
        btn = Button(text='MyButton')
        # didalam layout itu menggunakan size hint -> untuk ukuran
        btn.size_hint = (1, 0.25)
        # didalam layout itu menggunakan pos_hint -> untuk posisi x, y, center_x, center_y, right, top
        btn.pos_hint = {'center_y': 0.5}
        btn2 = Button(text='MyButton2')
        btn3 = Button(text='MyButton3')
        btn4 = Button(text='MyButton4')
        blyt.add_widget(btn)
        blyt.add_widget(btn2)
        blyt.add_widget(btn3)
        blyt.add_widget(btn4)
        return blyt


MyApp().run()
