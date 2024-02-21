from kivy.uix.button import Button
from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Menu(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        
        layout = FloatLayout()

        # Imagem de fundo
        background = Image(source='pagina_inicialMobile.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Titulo da pagina
        msg_ajuda = Label(text = "[b]Escolha seu proprio nome[b]",
                          markup=True,
                          pos_hint={'center_x': 0.5, 'center_y': 0.70},
                          font_size=90)
        layout.add_widget(msg_ajuda)
        
        # Adicionar um TextInput ao layout
        self.text_input_01 = TextInput(multiline=False, 
                                       hint_text='Name Player 1',
                                       size_hint=(None, None),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.59},
                                       size=(250, 40))
        layout.add_widget(self.text_input_01)
        
        # Adicionar um TextInput ao layout
        self.text_input_02 = TextInput(multiline=False, 
                                       hint_text='Name Player 2',
                                       size_hint=(None,None),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.47},
                                       size=(250, 40))
        layout.add_widget(self.text_input_02)    
    
        # Adicionar botão de imagem sobre a imagem de fundo
        btn_play = Button(background_normal='img_btnPlay_home.png',
                             background_down='img_btnPlay_home.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.27},
                             size=(600, 100))
        btn_play.bind(on_press=self.btn_play_game)
        layout.add_widget(btn_play)
        
        self.add_widget(layout)
    
    def btn_play_game(self):
        pass