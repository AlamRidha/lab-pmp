from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class MainWindow(BoxLayout):
    button_one = "Button Satu"

    def tekan_button_satu(self):
        print("Button Satu ditekan")

    def tekan_button_dua(self):
        self.button_dua = self.ids.labelone.text
        print("Button yang ditekan berdasarkan dari label '", self.button_dua, "'")

    def open_popup(self):
        print("Popup dibuka")
        popup = MyPopup()
        popup.open()

    pass


# membuat pop up
class MyPopup(Popup):
    def close_popup(self):
        print("Popup ditutup")
        self.dismiss()
    pass


class MainApp(App):
    pass


MainApp().run()
