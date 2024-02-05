from kivymd.app import MDApp
from icecream import ic
from kivy.lang import Builder
from os.path import dirname, join
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
import json
from icecream import ic
from kivy.uix.button import Button
from kivy.metrics import dp, sp

current_dir = dirname(__file__)
kv_file_path = join(current_dir, 'task.kv')
Builder.load_file(kv_file_path)

class Note(Button):
    
    def check_status(self,instance):
        if MDApp.get_running_app().root.ids.task.ids.btn_deletenote.state != 'down':
            self.check_content()
        else:
            self.removeself(instance)
            MDApp.get_running_app().root.ids.task.ids.lbl_info.text= 'Silme Modu Aktif'
    def check_content(self):
        self.temp_text = self.text
        json_data = open('storage/notes.json')
        data = json.load(json_data)
        for key, value in data.items():
            if self.temp_text == key:
                MDApp.get_running_app().root.ids.task.ids.tf_title.text=key
                self.parent.parent.parent.parent.parent.ids.ti_body.text= value['value1']
                    
    def removeself(self,instance):
        self.temp_text = self.text
        json_data = open('storage/notes.json')
        data = json.load(json_data)
        del data[self.temp_text]
        with open('storage/notes.json', 'w') as file:
            json.dump(data, file)
        
        # for key, value in data.items():
        #     if self.temp_text == key:
        #         del data[key]
        #     with open('storage/notes.json', 'w') as file:
        #         json.dump(data, file)
        MDApp.get_running_app().root.ids.task.ids.box_notes.remove_widget(instance)
                
               
        
    #--Alternatively            
        #--Alternatively
        # self.temp_text = self.text
        # self.store = JsonStore('storage/notes.json')
        # nested_value = self.store.get(self.text)
        # MDApp.get_running_app().root.ids.task.ids.tf_title.text=self.text
        # MDApp.get_running_app().root.ids.task.ids.ti_body.text= nested_value['value1']
class Task(BoxLayout):
    def output_to_file(text):
        with open('log/debug_log.txt', 'a') as f:
            f.write(text + '\n')

    ic.configureOutput(prefix='Debug-Task |', outputFunction=output_to_file, includeContext=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def on_load(self):
        self.ids.tf_title.readonly = False
        self.ids.ti_body.readonly = False
        try:
            json_data = open('storage/notes.json')
            data = json.load(json_data)
            ic(data)
            for key, value in data.items():
                new_list = key
                ic(new_list)
                btn = Note(text=key, size_hint=(1,None), height=dp(50))
                self.ids.box_notes.add_widget(btn)   
        except:
            self.ids.lbl_info = 'Notlar Yüklenemedi'

        
    def add_note(self):
        self.ids.lbl_info.color = 'white'
        self.store = JsonStore('storage/notes.json')
        if self.ids.btn_addnote.state == 'down':
            self.ids.tf_title.readonly = False
            self.ids.ti_body.readonly = False
            self.ids.lbl_info.text = "Not Ekleme Modu"
        else:
            try:
                if self.ids.tf_title.text in self.store:
                    self.ids.lbl_info.color = 'red'
                    self.ids.lbl_info.text = "Başlık Eşsiz Olmalı"
                    ic('başlık')
                else:
                    self.store.put(self.ids.tf_title.text, value1=self.ids.ti_body.text) 
                    self.ids.lbl_info.color = 'green'   
                    self.ids.lbl_info.text = "Not Eklendi"
                    btn = Note(text=self.ids.tf_title.text, size_hint=(1,None), height=dp(50))
                    self.ids.box_notes.add_widget(btn)
                    self.ids.tf_title.text=''
                    self.ids.ti_body.text=''
                    self.ids.lbl_info.text = ''    
            except:
                ic('Error')
    
    def read_note(self):
        self.store = JsonStore('storage/notes.json')
        if self.ids.btn_readnote.state == 'down':
            self.ids.tf_title.readonly = True
            self.ids.ti_body.readonly = True
            self.ids.lbl_info.text = "Not Okuma Modu"
            if self.ids.tf_title.text in self.store:
                self.ids.box_notes.clear_widgets()
                self.ids.tf_title.text=''
                self.ids.ti_body.text=''
                self.on_load()
        else:
            self.ids.lbl_info.text = ''
                    
        
    def update_note(self):
        self.store = JsonStore('storage/notes.json')
        if self.ids.btn_updatenote.state == 'down':
            self.ids.lbl_info.text = "Not Güncelleme Modu"
            self.ids.tf_title.readonly = True
            self.ids.ti_body.readonly = False
            if self.ids.tf_title.text in self.store:
                self.ids.tf_title.readonly = True
                self.ids.ti_body.readonly = False
        else:
            try:
                self.store.put(self.ids.tf_title.text, value1=self.ids.ti_body.text) 
                self.ids.lbl_info.color = 'green'   
                self.ids.lbl_info.text = "Not Güncellendi"
                self.ids.tf_title.text=''
                self.ids.ti_body.text=''
                self.ids.tf_title.readonly = True
                self.ids.ti_body.readonly = True    
            except:
                ic('Error in updating notes')
                
                
            
            
    
    def delete_note(self):
        try:
            self.ids.lbl_info.color = 'white'
            json_data = open('storage/notes.json')
            data = json.load(json_data)
            if self.ids.btn_deletenote.state == 'down':
                self.ids.lbl_info.text = "Silme Modu"
                self.ids.lbl_info.color = 'red'
                # Note.removeself()
                # del data[self.ids.tf_title.text]
                # with open('storage/notes.json', 'w') as file:
                #     json.dump(data, file)
                self.refresh_notes()    
            else:
                self.ids.lbl_info.text = ""
                self.ids.lbl_info.color = 'white'
                self.refresh_notes()  
        except:
            ic('Error in deleting notes')
    def refresh_notes(self):
        pass
        # self.ids.box_notes.clear_widgets()
        # self.on_load()
            
        
        