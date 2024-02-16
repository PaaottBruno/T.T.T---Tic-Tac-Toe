from menu import Menu
from game import Game

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Home(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        # Criar a tela aqui
        

class TicTacToeApp(App):
    def build(self):
        # Window.size = (430, 932)

        tela = ScreenManager()
        tela.add_widget(Home(name = "home")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.add_widget(Game(name = "game")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.current = "game"
        return tela
    
TicTacToeApp().run()