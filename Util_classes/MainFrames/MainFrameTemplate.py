import customtkinter as ctk


class MainFrameTemplate(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=6, border_width=2,
                       border_color="black", fg_color="#FFE3A3")

        self.columnconfigure([0, 1, 2], weight=2)
        for i in range(10):
            self.rowconfigure(i, weight=1)

    class MenuButton(ctk.CTkButton):
        def __init__(self, master, text: str, command=None):
            super().__init__(master)
            self.configure(text=text, text_color="black", font=master.btn_font,
                           fg_color=master.fg_color, hover_color=master.fg_color_hover,
                           corner_radius=6, border_width=2, border_color="black",
                           height=50,
                           command=command)
