from kivymd.app import MDApp
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from kivy.properties import ColorProperty, ListProperty, NumericProperty
from .view import MainWindow
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MainApp(MDApp):
    
    #theme stuff
    
    
    
    
    def build(self):
        self.theme_cls.material_style= "M2"
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Steelblue"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.primary_dark_hue = "100"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "500"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.2
        self.theme_cls.dynamic_color = False
        #theme _cls 
        # labelbase font register
        
        
        return MainWindow()
    
    def toggle_theme(self):
        pass