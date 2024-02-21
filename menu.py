from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        layout = FloatLayout()

        # Adiciona a imagem de fundo ao layout
        image_pag_home = Image(source='img_pagName_player.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(image_pag_home)

        button_seta_voltar = Button(size_hint=(None, None),
                                    pos_hint={'center_x': 0.08, 'center_y': 0.95},
                                    size=(120, 85),
                                    background_normal='seta-voltar.png',
                                    background_down='seta-voltar.png')
        button_seta_voltar.bind(on_press=self.on_button_press_voltar)
        layout.add_widget(button_seta_voltar)

        # Cria um TextInput com caixa de texto invisível e letras visíveis
        name_player_1 = TextInput(hint_text='Name Player 1',
                                  background_color=(1, 1, 1, 0),
                                  foreground_color=(1, 1, 1, 1),
                                  multiline=False, size_hint=(None, None), size=(410, 80),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                  border=(0, 0, 0, 0),
                                  font_size=40)
        layout.add_widget(name_player_1)

        name_player_2 = TextInput(hint_text='Name Player 2',
                                  background_color=(1, 1, 1, 0),
                                  foreground_color=(1, 1, 1, 1),
                                  multiline=False, size_hint=(None, None), size=(410, 80),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                  border=(0, 0, 0, 0),
                                  font_size=40)
        layout.add_widget(name_player_2)

        image_linha = Image(source='img_line_player.png', allow_stretch=True, keep_ratio=True,
                            size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(image_linha)

        # Adicionar botão de imagem sobre a imagem de fundo
        button_play = Button(background_normal='img_btnPlay_home.png',
                             background_down='img_btnPlay_home.png',
                             size_hint=(None, None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.1},
                             size=(600, 100))
        button_play.bind(on_press=self.on_button_press_play)
        layout.add_widget(button_play)

        # Adiciona o layout à tela
        self.add_widget(layout)

    def on_button_press_voltar(self, instance):
        self.manager.current = "home"

    def on_button_press_play(self, instance):
        self.manager.current = "game"
        self.attempts = 0
