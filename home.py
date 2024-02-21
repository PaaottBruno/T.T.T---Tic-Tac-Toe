from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class Home(Screen):#FloatLayout
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        layout = FloatLayout()

        # Adicionar a imagem de fundo ao layout,  allow_stretch=True, keep_ratio=False
        image_pag_home = Image(source='img_pagHome_label.png', allow_stretch=True, keep_ratio=False)

        titulo_game = Label(text='Tic tac Toe', font_size=24)

        # Adicionar o Label ao layout
        layout.add_widget(titulo_game)

        # Adicionar botão de imagem sobre a imagem de fundo
        button_play = Button(background_normal='btn_play.png',
                             background_down='btn_play.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.43},# o size_hint serve para mecher na largura do botão
                             size=(500, 120))
        button_play.bind(on_press=self.on_button_press_play)  # Adiciona uma função de callback ao pressionar o botão

        button_exit = Button(background_normal='btn_exit.png',
                             background_down='btn_exit.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.29},
                             size=(500, 120))
        button_exit.bind(on_press=self.on_button_press_exit)  # Adiciona uma função de callback ao pressionar o botão
        
        layout.add_widget(image_pag_home)
        layout.add_widget(button_play)
        layout.add_widget(button_exit)
        self.add_widget(layout)

    def on_button_press_play(self, instance):
        self.manager.current = "menu" 
        
    # DEF SAIR
    def on_button_press_exit(self, instance):
        # Função para encerrar o aplicativo
        App.get_running_app().stop()
  

    
        


