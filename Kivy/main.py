import kivy
from pages.home import Home
from pages.game import Game

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class TicTacToeApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(Home(name = "home"))
        sm.add_widget(Game(name = "game"))
        sm.current = "home"

        return sm
    
TicTacToeApp().run()