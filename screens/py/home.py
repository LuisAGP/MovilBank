import os
import json
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

with open(os.path.join(os.getcwd(), "screens", "kv", "home.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class HomeScreen(MDScreen):
    pass