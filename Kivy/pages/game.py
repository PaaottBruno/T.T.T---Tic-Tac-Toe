from kivy.uix.button import Button
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.relativelayout import RelativeLayout

class Game(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        tabela = [[ " " for _ in range(3)] for _ in range(3)] # Criando o tabuleiro
        
        
        layout = FloatLayout()

        # Imagem de fundo
        background = Image(source='../img/fundo.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Botão Voltar
        button = Button(text='', 
                        size_hint=(0.12, 0.06), 
                        pos_hint={'center_x': 0.1, 'center_y': 0.95}, 
                        background_normal='../img/seta-voltar.png',
                        background_down='../img/seta-voltar.png'
                        )
        
        # Criando a tebela do jogo
        table_btn = GridLayout(cols=3, size_hint=(None, None), spacing=7, size=(300, 300))
        table_img = RelativeLayout(size_hint=(None, None), size=(300, 300))
        table_img_fundo = Image(source='../img/Tabela.png', allow_stretch=True, keep_ratio=False)
    
        table_img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            
        table_img.add_widget(table_img_fundo)
        table_img.add_widget(table_btn)
        layout.add_widget(table_img)
        
        # Adicionando os botões na tela
        for linha in range(3):
            for coluna in range(3):
                botao = Button(text='Ola', 
                               font_size=(50),
                               size_hint=(0.02, 0.02), 
                               pos_hint={'center_x': 0.8, 'center_y': 0.8},
                               background_color=(1, 1, 1, 0)) # (1, 1, 1, 1): nâo transparente, (1, 1, 1, 0.5): 50% transparente, (1, 1, 1, 0): Transparente
                table_btn.add_widget(botao)
        
        layout.add_widget(button)
        self.add_widget(layout)

    def on_button_press(self, row, col, button):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            button.text = self.current_player
            if self.check_winner():
                print(f'{self.current_player} wins!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.minimax_move()

    def check_winner(self):
        # Implement your winning condition check here
        # Return True if there is a winner, False otherwise
        pass

    def reset_board(self):
        # Implement board reset logic here
        pass

    def minimax_move(self):
        # Implement Minimax algorithm to make the computer's move
        pass
    
class TicTacToeApp(App):
    def build(self):
        Window.size = (430, 932)
        
        tela = ScreenManager()
        tela.add_widget(Game(name = "home")) # para adicionar outro tem que: Colocar o nome da class(name = "Nome da classe tbm")
        tela.current = "home"
        return tela
    
TicTacToeApp().run()
