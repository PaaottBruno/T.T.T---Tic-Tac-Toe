from pages.menu import Menu
from pages.game import Game
from pages.home import Home
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.image import Image
from kivy.app import MDApp
from kivy.lang import Builder



class Home(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        Layout = BoxLayout(orientation = 'vertical')
        tamanho = '80'
        image = Image(source = 'img-jogoVelha.png' , pos_hint={'x':.375, 'y':.40})
        titulo = MDLabel(text="Tic Tac Toe", )

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(100)
        md_bg_color: app.theme_cls.primary_color  # Cor de fundo conforme o tema padrão

        MDLabel:
            text: "Título Personalizado"
            theme_text_color: "Custom"  # Define uma cor personalizada
            text_color: 1, 1, 1, 1  # Cor do texto (branco)
            font_style: "H4"  # Estilo da fonte, aqui H4 é um exemplo, você pode ajustar conforme necessário
            halign: 'center'
'''


class CustomFontApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

CustomFontApp().run()     
        
        

class TicTacToeApp(App):
    def build(self):

        tela = ScreenManager()
        tela.add_widget(Home(name = "home")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.current = "home"
        return tela
    

    
if __name__ == "__main__":
    TicTacToeApp().run()