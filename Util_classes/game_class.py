import customtkinter as ctk
from Util_classes.MainFrames.MainFrameBase import MainFrameBase


class GameFrame(MainFrameBase):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="ИГРА НОМЕР 228")
        self.label.grid(row=1, column=1)
