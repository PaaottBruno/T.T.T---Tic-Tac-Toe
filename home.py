from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager


class Home(Screen):#FloatLayout
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        layout = FloatLayout()

        # Adicionar a imagem de fundo ao layout,  allow_stretch=True, keep_ratio=False
        image_pag_home = Image(source='pagina_inicialMobile.png', allow_stretch=True, keep_ratio=False)

        # Adicionar botão de imagem sobre a imagem de fundo
        button_play = Button(background_normal='img_btnPlay_home.png',
                             background_down='img_btnPlay_home.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5},# o size_hint serve para mecher na largura do botão
                             size=(220, 60))
        button_play.bind(on_press=self.on_button_press_play)  # Adiciona uma função de callback ao pressionar o botão

        button_exit = Button(background_normal='img_btnExit_home.png',
                             background_down='img_btnExit_home.png',
                             size_hint=(None,None),
                             pos_hint={'center_x': 0.5, 'center_y': 0.2},
                             size=(220, 60))
        button_exit.bind(on_press=self.on_button_press_exit)  # Adiciona uma função de callback ao pressionar o botão
        
        layout.add_widget(image_pag_home)
        layout.add_widget(button_play)
        layout.add_widget(button_exit)
        self.add_widget(layout)

    def on_button_press_play(self, instance):
        self.manager.current = "home" # Tirar depois
        self.attempts = 0
        
        
    def on_button_press_exit(self, instance):
        print('Botão exit pressionado!')


    # DEF SAIR
    def sair(self, instance):
      # Função para encerrar o aplicativo
        App.get_running_app().stop()
        
    # DEF VAI PARA A PÁGINA DE ESCOLHER 1 OU 2 JOGADORES. 
    def ir_para_pag_player(self, instance):
        self.manager.current = "pag_player" 

    # DEF DECLARA A PAGINA HOME PARA RODAR NA MAIN.
    def voltar_tela_home(self, instance):
        self.manager.current = "home"    
        self.attempts = 0


    def ir_para_outra_tela(self, instance):
        self.manager.current = "outra_tela"


class OutraTela(Screen):
    def __init__(self):
        self.button_voltar = Button(text="Voltar")
        self.button_voltar.bind(on_press=self.voltar_para_tela_inicio)
        self.add_widget(self.button_voltar)

    def voltar_para_tela_inicio(self, instance):
        self.manager.current = 'tela_inicio'
    
        



# class TicTacToeApp(App):
#     def build(self):
#         return Home()

# if __name__ == '__main__':
#     TicTacToeApp().run()
