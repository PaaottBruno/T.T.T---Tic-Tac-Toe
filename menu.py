from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class Menu(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Window.size = (430, 932)
        
        #  Criar a tela Menu aqui