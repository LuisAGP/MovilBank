import os
import json
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout

with open(os.path.join(os.getcwd(), "screens", "kv", "transaction.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class TransactionAmount(IRightBodyTouch, MDBoxLayout):
    pass

class ListItemTransaction(TwoLineAvatarIconListItem):
    pass


class TransactionScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        with open('assets/data/transacciones.json', encoding="utf-8") as data:
            transacciones = json.load(data)

            for item in transacciones:
                list_item = ListItemTransaction()
                list_item.text=str(item['nombre'])
                list_item.secondary_text=str(item['empresa'])
                list_item.icon=item['icon']
                list_item.background_color=item['color']
                list_item.monto=str(item['monto'])

                self.ids.lista_transacciones.add_widget(list_item)

