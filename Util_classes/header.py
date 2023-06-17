import customtkinter as ctk
from PIL import Image


class MainHeader(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=master.get_main_colors()[0], corner_radius=0)
        self.LOGO_PICK = ctk.CTkImage(Image.open("static/QUIZZY.png"), size=(200, 50))
        self.Logo = ctk.CTkLabel(self, image=self.LOGO_PICK, text="", fg_color="transparent")
        self.Logo.grid(pady=(10, 10))