
# Tela home(inicial)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.layout import Layout
from kivy.uix.image import Image

class Home(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Layout = BoxLayout(orientation="vertical")
        tamanho = '80'
        
        #butons
        self.button_play = Button(text="Play")
        self.button_exit = Button(text="Exit")
        
        self.add_widget(Layout)
        
        Layout.add_widget(self.button_play)
        Layout.add_widget(self.button_exit)
        
        
        
        background = Image(source='pagina_jogo.png', allow_stretch=True, keep_ratio=False)
        Layout.add_widget(background)
        
       
      
        
        
        
    def iniciar_jogo_velha(self,instance):
        self.manager.current = 'jogo_da_velha'
        
        
    def sair(self, instance):
      # Função para encerrar o aplicativo
        App.get_running_app().stop()
        
        
    def ir_para_pag_player(self, instance):
        self.manager.current = "pag_player" 
        
    def tela_home(self, instance):
        self.manager.current = "pag_home" 
        
     
# KV = '''
# MDScreen:

#     MDIconButton:
#         icon: "language-python"
#         pos_hint: {"center_x": .5, "center_y": .5}
        
# '''

        
        


