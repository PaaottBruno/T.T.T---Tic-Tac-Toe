import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.uix.screenmanager import Screen

class Home(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        btn = Button(text="Ola")
        btn.bind(on_press=self.change)
        self.add_widget(btn)

    def change(self, instance):
        self.manager.current = "game"