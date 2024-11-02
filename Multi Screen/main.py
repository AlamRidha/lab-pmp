from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class PageOne(Screen):
    def changescreen(self):
        self.manager.current = 'pagetwo'


class PageTwo(Screen):
    pass


class MainScreen(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return MainScreen()


MainApp().run()
