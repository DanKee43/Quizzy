import customtkinter as ctk


class MainFrameBase(ctk.CTkFrame):
    class Menu_Button(ctk.CTkButton):
        def __init__(self, master, text, command=None):
            super().__init__(master)
            self.configure(text=text, text_color="black", font=master.btn_font,
                           fg_color=master.fg_color, hover_color=master.fg_color_hover,
                           corner_radius=6, border_width=2, border_color="black",
                           height=50,
                           command=command)

    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=4, border_width=2,
                       border_color="black", fg_color="#CECECE")
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        for i in range(10):
            self.rowconfigure(i, weight=1)
