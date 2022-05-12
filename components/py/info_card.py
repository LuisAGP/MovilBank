import os
from kivy.lang import Builder
from kivymd.uix.card import MDCard

with open(os.path.join(os.getcwd(), "components", "kv", "info_card.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())

class InfoCard(MDCard):
    pass