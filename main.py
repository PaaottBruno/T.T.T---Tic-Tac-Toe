from home import Home
from game import Game
from menu import Menu
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



class TicTacToeApp(App):
    def build(self):
        # Window.size = (430, 932)

        tela = ScreenManager()
        tela.add_widget(Home(name = "home")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.add_widget(Game(name = "game"))
        tela.add_widget(Menu(name = "menu")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.current = "menu"
        
       
        return tela
    

    
if __name__ == "__main__":
    TicTacToeApp().run()