from kivy.uix.button import Button
from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label

class Game(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.tabela = [[ " " for _ in range(3)] for _ in range(3)] # Criando o tabuleiro
        self.atual_jogador = 'X'
        self.pontos_total_x = 0
        self.pontos_total_o = 0
        
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

        # Placar do jogo
        container_placar = RelativeLayout(size_hint=(None, None), size=(800, 300))

        placar = Image(source="placar.png",
                        allow_stretch=True, 
                        keep_ratio=False,
                        pos_hint={'center_x': 0.52, 'top': 1.0})
        
        container_placar.pos_hint = {'center_x': 0.5, 'center_y': 0.87}
        
        
        # Criando a tebela do jogo
        table_btn = GridLayout(cols=3, size_hint=(None, None), spacing=7, size=(800, 800)) # normal 800 cada
        table_img = RelativeLayout(size_hint=(None, None), size=(800, 800))
        table_img_fundo = Image(source='tabela.png', allow_stretch=True, keep_ratio=False)
    
        table_img.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
            
        table_img.add_widget(table_img_fundo)
        table_img.add_widget(table_btn)
        container_placar.add_widget(placar)
        layout.add_widget(table_img)
        layout.add_widget(container_placar)
        
        # Adicionando os botões na tela
        self.botoes = []
        
        for linha in range(3):
            linha_botoes = []
            for coluna in range(3):
                self.botao = Button(text='', 
                               font_size=(90),
                               size_hint=(0.02, 0.02), 
                               pos_hint={'center_x': 0.8, 'center_y': 0.7},
                               background_color=(1, 1, 1, 0), # (1, 1, 1, 1): nâo transparente, (1, 1, 1, 0.5): 50% transparente, (1, 1, 1, 0): Transparente
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
            self.popup_win("X")
            self.pontos("X", 1)
            
        elif linha_1_o or linha_2_o or linha_3_o or coluna_1_o or coluna_2_o or coluna_3_o or diagonal_principal_o or diagonal_secundaria_o:
            self.popup_win("O")
            self.pontos("O", 1)
            
        if all(all(elemento != ' ' for elemento in linha) for linha in self.tabela) and \
        not any(all(self.tabela[linha][coluna] == ' ' for coluna in range(3)) for linha in range(3)):
            self.popup_win(None)
            return True

        # O jogo ainda não terminou
        return False
    def popup_win(self, ganhador):
        
        # Parando a funcionalidade dos botões do jogo
        for linha in self.botoes:
            for botao in linha:
                botao.disabled = True
                
        if ganhador == "X":
            self.popup_reset()
            self.mensagem_x = Label(text = "[b]Player 1 Win[b]",
                                    markup=True,
                                    pos_hint={'center_x': 0.5, 'center_y': 0.75},
                                    font_size=100)
            
            self.add_widget(self.mensagem_x)
            
        elif ganhador == "O":
            self.popup_reset()
            self.mensagem_o = Label(text = "[b]Player 2 Win[b]",
                                    markup=True,
                                    pos_hint={'center_x': 0.5, 'center_y': 0.75},
                                    font_size=100)
            self.add_widget(self.mensagem_o)
        
        else:
            self.popup_reset()
            self.mensagem_empate = Label(text = "[b]Empate[b]",
                                    markup=True,
                                    pos_hint={'center_x': 0.5, 'center_y': 0.75},
                                    font_size=100)
            self.add_widget(self.mensagem_empate)
            
    def popup_reset(self):
        
        self.fundo_cinza = Image(source="fundo_cinza.png", allow_stretch=True, keep_ratio=False)

        self.btn_reset = Button(size_hint=(None, None), 
                                pos_hint={'center_x': 0.5, 'center_y': 0.6}, 
                                size=(200, 200),
                                background_normal='seta-reset.png',
                                background_down='seta-reset.png'
                                )
        
        self.btn_voltar = Button(size_hint=(None, None), 
                                pos_hint={'center_x': 0.5, 'center_y': 0.48}, 
                                size=(200, 90),
                                background_normal='btn_voltar.png',
                                background_down='btn_voltar.png'
                                )
        
        self.btn_reset.bind(on_press= self.reset_tabela)
        self.add_widget(self.fundo_cinza)
        self.add_widget(self.btn_voltar)
        self.add_widget(self.btn_reset)
        
    def reset_tabela(self, instancia):
        
        self.tabela = [[ " " for _ in range(3)] for _ in range(3)] # resetando a lista
        self.remove_widget(self.fundo_cinza)
        self.remove_widget(self.btn_voltar)
        self.remove_widget(self.btn_reset) # removendo o botão de reset game
        
        if hasattr(self, 'mensagem_x'):
            self.remove_widget(self.mensagem_x)

        if hasattr(self, 'mensagem_o'):
            self.remove_widget(self.mensagem_o)
            
        if hasattr(self, 'mensagem_empate'):
            self.remove_widget(self.mensagem_empate)
            
        # removendo os simbolos da tabela
        for linha in self.botoes:
            for botao in linha:
                botao.text = ''
        
        # Voltando a funcionalidade dos botões do jogo
        for linha in self.botoes:
            for botao in linha:
                botao.disabled = False
                
    def pontos(self, jogador, quantidade):
        
        if jogador == "X":
            
            if hasattr(self, 'player_1'):
                self.remove_widget(self.player_1) 
                
            self.pontos_total_x += quantidade
            
            self.player_1 = Label(text=str(self.pontos_total_x),
                            pos_hint={'center_x': 0.41, 'center_y': 0.87},
                            font_size=80,
                            color=(0, 0, 0, 1))
            
            self.add_widget(self.player_1)
            
        elif jogador == "O":
            
            if hasattr(self, 'player_2'):
                self.remove_widget(self.player_2) 
                
            self.pontos_total_o += quantidade
            
            self.player_2 = Label(text=str(self.pontos_total_o),
                            pos_hint={'center_x': 0.57, 'center_y': 0.87},
                            font_size=80,
                            color=(0, 0, 0, 1))
            
            self.add_widget(self.player_2) 
        
    def minimax_move(self):
        # Implement Minimax algorithm to make the computer's move
        pass