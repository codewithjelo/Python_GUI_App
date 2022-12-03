import customtkinter
from PIL import Image
from utils.main_menu import *


class WelcomeScreen():
    def __init__(self, ctk):
        self.frame = customtkinter.CTkFrame(master=ctk)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

    def welcome_screen(self):
        # Logo Image
        image_icon_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/PC_FIND.png"),
            size=(150, 45))
        label_image = customtkinter.CTkLabel(master=self.frame, text="", image=image_icon_image)
        label_image.pack(pady=(20, 0), padx=10)
        # Welcome Screen
        welcome_label = customtkinter.CTkLabel(master=self.frame, text="Welcome to PCFIND", font=('Montserrat', 14),
                                               text_color='#2FA572')
        welcome_label.pack(pady=(20, 0), padx=10)
        description_label = customtkinter.CTkLabel(master=self.frame,
                                                   text="\"SOFTWARE comes from heaven when you have good HARDWARE\"",
                                                   font=('Courier New', 10),
                                                   text_color='white')
        description_label.pack(padx=10)

        shop_button = customtkinter.CTkButton(master=self.frame, text='SHOP', font=('Montserrat', 18))
        shop_button.pack(pady=(100, 0), padx=10)