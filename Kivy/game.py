from kivy.uix.button import Button
from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window

class Game(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Window.size = (430, 932)

        self.tabela = [[ " " for _ in range(3)] for _ in range(3)] # Criando o tabuleiro
        self.atual_jogador = 'X'
        
        layout = FloatLayout()

        # Imagem de fundo
        background = Image(source='fundo.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Botão Voltar
        button = Button(size_hint=(None, None), 
                        pos_hint={'center_x': 0.1, 'center_y': 0.95}, 
                        size=(100, 50),
                        background_normal='seta-voltar.png',
                        background_down='seta-voltar.png'
                        )
        
        # Criando a tebela do jogo
        table_btn = GridLayout(cols=3, size_hint=(None, None), spacing=7, size=(800, 800))
        table_img = RelativeLayout(size_hint=(None, None), size=(800, 800))
        table_img_fundo = Image(source='Tabela.png', allow_stretch=True, keep_ratio=False)
    
        table_img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            
        table_img.add_widget(table_img_fundo)
        table_img.add_widget(table_btn)
        layout.add_widget(table_img)
        
        # Adicionando os botões na tela
        self.botoes = []
        
        for linha in range(3):
            linha_botoes = []
            for coluna in range(3):
                self.botao = Button(text='', 
                               font_size=(50),
                               size_hint=(0.02, 0.02), 
                               pos_hint={'center_x': 0.8, 'center_y': 0.8},
                               background_color=(1, 1, 1, 0.5), # (1, 1, 1, 1): nâo transparente, (1, 1, 1, 0.5): 50% transparente, (1, 1, 1, 0): Transparente
                               on_press=partial(self.on_button_press, linha, coluna)) 
                linha_botoes.append(self.botao)
                table_btn.add_widget(self.botao)
            self.botoes.append(linha_botoes)
        
        layout.add_widget(button)
        self.add_widget(layout)

    def on_button_press(self, linha, coluna, button):
        if self.tabela[linha][coluna] == ' ':
            self.tabela[linha][coluna] = self.atual_jogador
            button.text = self.atual_jogador
            
            if self.verificar_ganhador():
                pass
            else:
                self.atual_jogador = 'O' if self.atual_jogador == 'X' else 'X'
                # self.minimax_move()

    def verificar_ganhador(self):
        # X 
        linha_1_x = all(elemento == 'X' for elemento in self.tabela[0])
        linha_2_x = all(elemento == 'X' for elemento in self.tabela[1])
        linha_3_x = all(elemento == 'X' for elemento in self.tabela[2])

        coluna_1_x = all(self.tabela[linha][0] == 'X' for linha in range(3))
        coluna_2_x = all(self.tabela[linha][1] == 'X' for linha in range(3))
        coluna_3_x = all(self.tabela[linha][2] == 'X' for linha in range(3))

        diagonal_principal_x = all(self.tabela[i][i] == 'X' for i in range(3))
        diagonal_secundaria_x = all(self.tabela[i][2 - i] == 'X' for i in range(3))
        
        # O
        linha_1_o = all(elemento == 'O' for elemento in self.tabela[0])
        linha_2_o = all(elemento == 'O' for elemento in self.tabela[1])
        linha_3_o = all(elemento == 'O' for elemento in self.tabela[2])

        coluna_1_o = all(self.tabela[linha][0] == 'O' for linha in range(3))
        coluna_2_o = all(self.tabela[linha][1] == 'O' for linha in range(3))
        coluna_3_o = all(self.tabela[linha][2] == 'O' for linha in range(3))

        diagonal_principal_o = all(self.tabela[i][i] == 'O' for i in range(3))
        diagonal_secundaria_o = all(self.tabela[i][2 - i] == 'O' for i in range(3))

        if linha_1_x or linha_2_x or linha_3_x or coluna_1_x or coluna_2_x or coluna_3_x or diagonal_principal_x or diagonal_secundaria_x:
            print("Ganhou!")
            self.popup_reset()
            
        elif linha_1_o or linha_2_o or linha_3_o or coluna_1_o or coluna_2_o or coluna_3_o or diagonal_principal_o or diagonal_secundaria_o:
            print("Ganhou!")
            self.popup_reset()
            
        else:
            for linha in self.tabela:
                for elemento in linha:
                    if elemento == ' ':      
                        verificar = False
                    else: 
                        verificar = True        
            if verificar:
                print("Deu velha")
                self.popup_reset()
            
    def popup_reset(self):
        self.btn_reset = Button()
        self.btn_reset.bind(on_press= self.reset_board)
        self.add_widget(self.btn_reset)
        
    def reset_board(self, instancia):
        self.tabela = [[ " " for _ in range(3)] for _ in range(3)] # resetando a lista
        self.remove_widget(self.btn_reset) # removendo o botão de reset game
        
        # removendo os simbolos da tabela
        for linha in self.botoes:
            for botao in linha:
                botao.text = ''
        
    def minimax_move(self):
        # Implement Minimax algorithm to make the computer's move
        pass

