import customtkinter
from utils import WelcomeScreen

if __name__ == "__main__":
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    root = customtkinter.CTk()
    root.title('PCFind')
    # Welcome
    welcome = WelcomeScreen(root)
    welcome.welcome_screen()

    # Mainloop
    root.mainloop()
