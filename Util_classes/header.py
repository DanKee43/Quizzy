import customtkinter as ctk
from PIL import Image


class MainHeader(ctk.CTkFrame):
    def __init__(self, APP):
        super().__init__(APP)
        self.configure(fg_color=APP.get_main_colors()[0], corner_radius=0)
        self.LOGO_PIC = ctk.CTkImage(Image.open("static/QUIZZY.png"), size=(200, 50))
        self.Logo = ctk.CTkLabel(self, image=self.LOGO_PIC, text="", fg_color="transparent")
        self.Logo.grid(pady=(10, 10), padx=10)
