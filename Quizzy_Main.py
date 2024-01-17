import customtkinter as ctk

from Util_classes.header import MainHeader
from Util_classes.sidemenu import SideBarMenu
from Util_classes.MainFrames.mainmenu import MainMenu
from Util_classes.MainFrames.profileframe import (ProfileFrame, RegistrationPage, LoginPage)
from Util_classes.game_class import GameFrame

from Util_classes.User import User

import requests

Window_Width = 1500
Window_Height = 900


def check_connection() -> bool:
    try:
        requests.head("https://www.google.com/", timeout=1)
        return True
    except requests.ConnectionError:
        return False


class Main_Window(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("QUIZZY")
        self.configure(fg_color="#CECECE")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (Window_Width / 2)
        y = (screen_height / 2) - (Window_Height / 2)
        self.geometry('%dx%d+%d+%d' % (int(Window_Width * 0.6), int(Window_Height * 0.6), x, y))
        self.minsize(int(Window_Width * 0.6), int(Window_Height * 0.6))

        self.rowconfigure(1, weight=20)
        self.columnconfigure(1, weight=29)

        self.main_color = "#FFA302"
        self.main_color_hover = "#E18502"

        # self.app_language = "RUS"

        self._Main_header = MainHeader(self)
        self._Main_header.grid(row=0, columnspan=2, sticky=ctk.NSEW)

        self._Side_Menu = SideBarMenu(self)
        self._Side_Menu.grid(row=1, pady=(10, 0), padx=(0, 10), column=0, sticky=ctk.NSEW)

        self._Main_frame = MainMenu(self)
        self._Main_frame.grid(row=1, pady=(10, 10), padx=(10, 10), column=1, sticky=ctk.NSEW)

        self.App_Controller = App()

    def get_main_colors(self):
        return self.main_color, self.main_color_hover

    def change_main_color(self):
        pass

    # Main frames : Main_Menu, Game_frame, profile, options...
    def change_main_frame(self, frame_name):

        self._Main_frame.destroy()

        if frame_name == "menu":
            self._Main_frame = MainMenu(self)
        elif frame_name == "profile":
            self._Main_frame = ProfileFrame(self)
        elif frame_name == "login":
            self._Main_frame = LoginPage(self)
        elif frame_name == "registration":
            self._Main_frame = RegistrationPage(self)
        elif frame_name == "Game_frame":
            self._Main_frame = GameFrame(self)

        self._Main_frame.grid(row=1, pady=(10, 10), padx=(10, 10), column=1, sticky=ctk.NSEW)


class App:
    def __init__(self):
        self._User = User()
        self.lol = 1

    def is_user_auth(self):
        return self._User.is_user_authenticated()




if __name__ == "__main__":
    main_window = Main_Window()
    main_window.mainloop()
