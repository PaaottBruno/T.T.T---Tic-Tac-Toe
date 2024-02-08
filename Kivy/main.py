from pages.menu import Menu
from pages.game import Game

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Home(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        # Criar a tela aqui
        

class TicTacToeApp(App):
    def build(self):

        tela = ScreenManager()
        tela.add_widget(Home(name = "home")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.current = "home"
        return tela
    
TicTacToeApp().run()