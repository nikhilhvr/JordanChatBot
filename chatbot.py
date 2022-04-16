from tkinter import N
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase

Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class ResponseImage(Image):
    source = StringProperty()


class JordanChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen(
                'chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"

    def response(self, *args):
        if value == "Hello" or value == "hello" or value == "hey" or value == "Hey":
            # {screen_manager.get_screen('chats').bot_name.text}
            response = f"Hello {screen_manager.get_screen('chats').bot_name.text}. Wassssup!."

        elif value == "How are you?" or value == "how are you?":
            response = "I'm doing well. Thanks!"/N // "What about you"

        elif value == "What's your name" or value == "what's your name" or value == "what's your name?":
            response = "my name is Jordan ChatBot. anything else I can do for you!"

        elif value == "What's your name" or value == "what's your name" or value == "what's your name?":
            response = "I'm doing well. Thanks!"/N // "What about you"

        elif value == "Abhishek" or value == "abhishek":
            response = "Tha Man The Myth. He is the Execptional one."

        elif value == "Nikhil" or value == "nikhil":
            response = "Silently Dangerous you are! nobody should bother you in my opinion sir"

        elif value == "Sudha" or value == "sudha":
            response = "Miss Silent-Smart"

        elif value == "Abhishek" or value == "abhishek":
            response = "Tha Man The Myth"

        elif value == "Kapil" or value == "kapil" or value == "KAPIL":
            response = "F**k U Bitch!!  What are You Looking at"

        elif value == "purushottam" or value == "Purushottam":
            response = "Bhaiii Book chahiye !!"

        elif value == "Mardav" or value == "mardav":
            response = "Haaaan Vaiiii Savage !!"

        elif value == "Aman" or value == "aman" or value == "AMAN":
            response = "Cutieeee ho Kyaaa !!"

        elif value == "Aman singh" or value == "aman singh" or value == "AMAN SINGH":
            response = "Choti bachi ho Kyaaa !!"

        elif value == "Images":
            screen_manager.get_screen('chats').chat_list.add_widget(
                ResponseImage(source="chatbots.jpg"))
        elif value == "Images1":
            screen_manager.get_screen('chats').chat_list.add_widget(
                ResponseImage(source="1.png"))
        else:
            response = "I'm a prototype. can you say it again?"
        screen_manager.get_screen('chats').chat_list.add_widget(
            Response(text=response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(
                Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""


if __name__ == '__main__':
    LabelBase.register(
        name="Poppins", fn_regular="E:\Programming\JordanChatBot\Poppins\Poppins-ExtraBold.ttf")
    LabelBase.register(
        name="BPoppins", fn_regular="E:\Programming\JordanChatBot\Poppins\Poppins-ExtraBold.ttf")
    JordanChatBot().run()
