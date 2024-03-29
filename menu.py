from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Line, Color

class Menu(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        layout = FloatLayout()

        # Imagem de fundo
        background = Image(source='fundo_input_linha.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Botão voltar
        button_seta_voltar = Button(size_hint=(None, None),
                                    pos_hint={'center_x': 0.08, 'center_y': 0.95},
                                    size=(120, 85),
                                    background_normal='seta-voltar.png',
                                    background_down='seta-voltar.png')
        button_seta_voltar.bind(on_press=self.on_button_press_voltar)
        layout.add_widget(button_seta_voltar)
        
        # Titulo da pagina
        msg_ajuda = Label(text = "[b]Escolha seu proprio nome[b]",
                          markup=True,
                          pos_hint={'center_x': 0.5, 'center_y': 0.80},
                          font_size=90)
        layout.add_widget(msg_ajuda)
        
        # Adicionar um TextInput ao layout
        self.text_input_01 = TextInput(multiline=False, 
                                       hint_text='Name Player 1',
                                       size_hint=(None, None),
                                       pos_hint={'center_x': 0.40, 'center_y': 0.63},
                                       size=(400, 50), 
                                       background_color=(0, 0, 0, 0))
        self.text_input_01.bind(text=self.on_text_change)
        layout.add_widget(self.text_input_01)
        
        # Adicionar um TextInput ao layout
        self.text_input_02 = TextInput(multiline=False, 
                                       hint_text='Name Player 2',
                                       size_hint=(None,None),
                                       pos_hint={'center_x': 0.40, 'center_y': 0.50},
                                       size=(400, 50), 
                                       background_color=(0, 0, 0, 0))
        self.text_input_02.bind(text=self.on_text_change)
        layout.add_widget(self.text_input_02)  
        
        # Adicionar botão de imagem sobre a imagem de fundo
        btn_play = Button(background_normal='img_btnPlay_home.png',
                             background_down='img_btnPlay_home.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.27},
                             size=(600, 100))
        btn_play.bind(on_press=self.on_button_press_play)
        layout.add_widget(btn_play)
        
        self.add_widget(layout)

    def on_button_press_voltar(self, instance):
        self.manager.current = "home"

    def on_button_press_play(self, instance):
        game_screen = self.manager.get_screen("game")  # Obtém a instância da tela Game
        game_screen.set_player_names(self.text_input_01.text, self.text_input_02.text)
        self.manager.current = "game"
        
    def on_text_change(self, instance, value):
        # Limitando o número de caracteres a 10
        if len(value) > 6:
            instance.text = value[:6]
