from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    button_one = "Button Satu"

    def tekan_button_satu(self):
        print("Button Satu ditekan")

    def tekan_button_dua(self):
        self.button_dua = self.ids.labelone.text
        print("Button yang ditekan berdasarkan dari label '", self.button_dua, "'")
    pass


class MainApp(App):
    pass


MainApp().run()
