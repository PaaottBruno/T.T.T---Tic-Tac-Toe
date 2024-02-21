from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class InvisibleBackgroundTextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Criar um TextInput com caixa de texto invisível e letras visíveis
        invisible_background_input = TextInput(hint_text='Digite algo...',
                                               background_color=(1, 1, 1, 0),  # Cor de fundo totalmente transparente
                                               foreground_color=(1,1,1,1),  # Cor das letras
                                               multiline=False, size_hint=(None, None), size=(200, 40),
                                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                               border=(0, 0, 0, 0))  # Borda transparente

        layout.add_widget(invisible_background_input)

        return layout

if __name__ == '__main__':
    InvisibleBackgroundTextInputApp().run()
