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
            response = f"Hello {screen_manager.get_screen('chats').bot_name.text} Wassssup!. \n  Type 'chat' for few features"

        # Jordan ChatBot Interaction
        elif value == "How are you?" or value == "how are you?":
            response = "I'm doing well. Thanks! What about you"

        # elif value >= 0 &&  value <=9 :
        #     response = " We don't play Number game here buddy!"

        elif value == "chat" or value == "Chat":
            response = "As a prototype I have very little to give you unlike Our facebook \n \t 1.tye 'Jordan Game' \n \t 2. ask me about your or my name or your univercity \n \t 3. type 'Starex49' for a fun interaction"

        elif value == "my name" or value == "My name" or value == "what is my name":
            response = f"Your name is {screen_manager.get_screen('chats').bot_name.text} \t Am I correct?? "

        elif value == "What's your name" or value == "who are you" or value == "kaun hai tu?" or value == "name":
            response = "my name is Jordan ChatBot. anything else I can do for you!"

        elif value == "What's your name" or value == "what's your name" or value == "what's your name?":
            response = "I'm doing well. Thanks! What about you"

        elif value == "Starex" or value == "starex" or value == "StarEx":
            response = " Starex University is a private university located in the village Binola, Gurgaon district, Haryana, India. !!"

        elif value == "What can you do!" or value == "kya kar sakte ho tum" or value == "kya karoge":
            response = "Joh bhi tum bolo !!"

        elif value == "gf banwa de" or value == "GF banwa de" or value == "Gf banwade" or value == "gf chahiye" or value == "bandi chahiye":
            response = "Nahin milegi !!"

        elif value == "what is chatbot" or value == "chatbot kya hai" or value == "chatbot":
            response = "An AI chatbot (Artificial Intelligence chatbot) is a chatbot that’s powered by artificial intelligence (AI). Unlike regular chatbots, AI chatbots are able to understand user queries through natural language processing (NLP) and can give intelligent answers to them. "

        # Jordan Automate Features

        # Jordan Game start here -->
        elif value == "Jordan game" or value == "jordan game" or value == "JORDAN GAME":
            response = "welcome to Jordan game. You will going to on an Adventure !! \n \t Are you ready for thisss! \n \t YES/NO"

        elif value == "Yes" or value == "yes" or value == "YES":
            response = "Awesome! I knew it you are Alive as the Fish in my plate! \n \t I have a game WOULD YOU RATHER \n \t Wantt to play \n \t yes1/no2"

        elif value == "No" or value == "no" or value == "NO":
            response = "so sad! We are missing an golden oppotunity to spend time with each other.\n \t Next time though "

        elif value == "yes1" or value == "Yes1":
            response = " Here is your First - Would you rather! \n \t Would you rather have the ability to see 10 minutes into the future or 150 years into the future? \n \t \t 1. For 10min GG \n \t For 150 KK "

        elif value == "GG" or value == "gg":
            response = " Great one!"

        elif value == "KK" or value == "kk":
            response = " Great one!"

        elif value == "No2" or value == "no2":
            response = "so sad! We are missing an golden oppotunity to spend time with each other.\n \t Next time though \n \t Type 'chat' "
            # print("Are you ready for thisss!")
            # YES/NO
            # if(value=="yes"){
            #response = "Awesome! I knew it you are Alive as the Fish in my plate!"
            # }
            # else{
            #     response = "so sad! We are missing an golden oppotunity to spend time with each other. "
            #     response= "Next time though"
            # }

        # Starex CSE Projects ahead
        elif value == "Starex49" or value == "starex49" or value == "StarEx49":
            response = "I have a Compliment for Youu! \n \t Type your name and I will give you my honest opinion"

        elif value == "Abhishek" or value == "abhishek":
            response = "Tha Man The Myth. He is the Execptional one."

        elif value == "Nikhil" or value == "nikhil":
            response = "Silently Dangerous you are! nobody should bother you in my opinion sir"

        # elif value == "Abhishek" or value == "abhishek":
        #     response = "Tha Man The Myth"

        elif value == "Kapil" or value == "kapil" or value == "KAPIL":
            response = "People’s Dreams... Have No Ends \n \t And Only I Can Call My Dream Stupid!"

        elif value == "purushottam" or value == "Purushottam":
            response = "Bhaiii Book chahiye !!"

        elif value == "vikas" or value == "Vikas kumar" or value == "Vvkas kumar":
            response = "Prampra, Pratistha and Anushahshan!! \n \t Matlab Sincerity"

        elif value == "amish" or value == "Amish" or value == "AMISH":
            response = "MOVIE LEAKER !"

        elif value == "Akansha" or value == "akansha" or value == "AKANSHA":
            response = "Topper bhyii tum rhe !! \n \t Hoshiyaar balak!"

        elif value == "Mardav" or value == "mardav":
            response = "Haaaan Vaiiii Savage !!"

        elif value == "Aman" or value == "aman" or value == "AMAN":
            response = "Cutieeee ho Kyaaa !!"

        elif value == "Aman singh" or value == "aman singh" or value == "AMAN SINGH":
            response = "Choti bachi ho Kyaaa !!"

        elif value == "Aditya ola" or value == "aditya ola" or value == "ola" or value == "OLA":
            response = "Great great lord. we are nothing without  !!"

        elif value == "Aman singh" or value == "aman singh" or value == "AMAN SINGH":
            response = "Choti bachi ho Kyaaa !!"

        elif value == "Nishikant" or value == "Nishikant" or value == "AMAN SINGH":
            response = "Assam Rifles !!"

        elif value == "Sudha" or value == "sudha":
            response = "Miss Silent-Smart"

        elif value == "Kapil49" or value == "kapil49" or value == "KAPIL49":
            response = "F**k U Bitch!!  What are You Looking at"

        elif value == "Images":
            screen_manager.get_screen('chats').chat_list.add_widget(
                ResponseImage(source="chatbots.jpg"))
        elif value == "Images1":
            screen_manager.get_screen('chats').chat_list.add_widget(
                ResponseImage(source="1.png"))
        else:
            response = "I'm a prototype like a baby! can you say it again?"
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
