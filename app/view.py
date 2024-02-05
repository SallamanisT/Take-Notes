# app/view.py

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from os.path import dirname, join
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

Window.size =(480,650)


class MainWindow(MDBoxLayout):
    def __init__(self, **kw) -> None:
        print("Entering MainWindow __init__")
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
