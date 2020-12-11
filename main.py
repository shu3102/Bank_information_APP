from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.floatlayout import FloatLayout
from Kv import screen_helper
from Kv import screen_Helper
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem, OneLineIconListItem, OneLineAvatarIconListItem
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import ContainerSupport
from kivy.uix.scrollview import ScrollView



Window.size = (360, 600)


class MainScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class ExampleScreen(Screen):
    pass


class MyLabel(Screen):
    pass


class Button1Screen(Screen):
    def showtext(self):
        with open("data.txt", "r") as f:
            return (f.read())


class Button2Screen(Screen):
    def showtext(self):
        with open('ATM.txt', 'r') as f:
            return (f.read())


class Button3Screen(Screen):
    pass


class Button4Screen(Screen):
    pass


class Button5Screen(Screen):
    pass


class Button6Screen(Screen):
    pass


class Button7Screen(Screen):
    pass


class Button8Screen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class ATMScreen(Screen):
    pass


class FileScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Button1Screen(name='Button1'))
sm.add_widget(Button2Screen(name='Button2'))
sm.add_widget(Button3Screen(name='Button3'))
sm.add_widget(Button4Screen(name='Button4'))
sm.add_widget(Button5Screen(name='Button5'))
sm.add_widget(Button6Screen(name='Button6'))
sm.add_widget(Button7Screen(name='Button7'))
sm.add_widget(Button8Screen(name='Button8'))
sm.add_widget(ATMScreen(name='atm'))
sm.add_widget((FileScreen(name='file')))
sm.add_widget(ExampleScreen(name='example'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.layout = FloatLayout()
        screen = Builder.load_string(screen_helper)
        Screen = Builder.load_string(screen_Helper)
        self.layout.add_widget(screen)
        self.layout.add_widget(Screen)
        return self.layout

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()
