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
        background = Image(source='pagina_inicialMobile.png', allow_stretch=True, keep_ratio=False)
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
                          pos_hint={'center_x': 0.5, 'center_y': 0.70},
                          font_size=90)
        layout.add_widget(msg_ajuda)
        
        # Adicionar um TextInput ao layout
        self.text_input_01 = TextInput(multiline=False, 
                                       hint_text='Name Player 1',
                                       size_hint=(None, None),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.59},
                                       size=(250, 40), 
                                       background_color=(0, 0, 0, 0))
        layout.add_widget(self.text_input_01)
        
        # Adicionar um TextInput ao layout
        self.text_input_02 = TextInput(multiline=False, 
                                       hint_text='Name Player 2',
                                       size_hint=(None,None),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.47},
                                       size=(250, 40), 
                                       background_color=(0, 0, 0, 0))
        layout.add_widget(self.text_input_02)  
        
        with layout.canvas:
            Color(0, 0, 0)
            # Adicionando uma linha ao layout
            line1 = Line(points=[280, 278, 450, 278], width=1)  # Pontos são coordenadas x, y
            
            # Adicionando uma linha ao layout
            line2 = Line(points=[280, 350, 450, 350], width=1)  # Pontos são coordenadas x, y
                

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
        self.manager.current = "game"
