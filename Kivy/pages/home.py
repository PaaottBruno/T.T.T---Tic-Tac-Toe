
# Tela home(inicial)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.layout import Layout

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Layout = BoxLayout(orientation = 'vertical')
        tamanho = '80'
        

