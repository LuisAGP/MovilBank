from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from screens.py import transaction, home
from kivy.core.window import Window

class BankApp(MDApp):
    def build(self):
        self.main_color      = get_color_from_hex("#2f26d9")
        self.font_color      = get_color_from_hex("#FFFFFF")
        self.font_color_dark = get_color_from_hex("#3f4c5a")
        self.screen_height   = Window.height
        self.screen_width    = Window.width

        self.sm = ScreenManager()
        self.sm.add_widget(home.HomeScreen(name="homescreen"))
        self.sm.add_widget(transaction.TransactionScreen(name="transactionscreen"))

        return self.sm

    # Función para regresar a la pantalla principal
    def go_home(self):
        self.sm.transition.direction = 'right'
        self.sm.current = 'homescreen'

if __name__=="__main__":
    BankApp().run()