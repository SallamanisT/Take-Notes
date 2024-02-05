from kivymd.app import MDApp
from icecream import ic
from kivy.lang import Builder
from os.path import dirname, join
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

current_dir = dirname(__file__)
kv_file_path = join(current_dir, 'mask.kv')
Builder.load_file(kv_file_path)

class Mask(BoxLayout):
    def output_to_file(text):
        with open('log/debug_log.txt', 'a') as f:
            f.write(text + '\n')

    ic.configureOutput(prefix='Debug-Mask |', outputFunction=output_to_file, includeContext=True)

    def __init__(self, **kw):
        ic()
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
