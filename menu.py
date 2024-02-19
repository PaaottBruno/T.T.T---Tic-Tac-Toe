from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Window.size = (430, 932)
        
        layout = FloatLayout()

        # Imagem de fundo
        background = Image(source='fundo.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Botão Voltar
        button = Button(size_hint=(None, None), 
                        pos_hint={'center_x': 0.08, 'center_y': 0.95}, 
                        size=(120, 85),
                        background_normal='seta-voltar.png',
                        background_down='seta-voltar.png'
                        )
        
        # Botão um Jogador
        

        
if __name__ == "__main__":
    Menu().run()        