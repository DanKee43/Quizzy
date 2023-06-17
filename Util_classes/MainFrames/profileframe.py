
from Util_classes.MainFrames.MainFrameBase import MainFrameBase, ctk


class ProfileFrame(MainFrameBase):
    def __init__(self, APP):
        super().__init__(APP)
        self.APP = APP  # Reference to App instance
        self.fg_color, self.fg_color_hover = APP.get_main_colors()
        self.btn_font = ("Arial", 20, "bold")

        # lab = ctk.CTkLabel(self, text="NAME:")
        # lab.grid(row=1, column=1, pady=(120, 0))

        if not APP.IsAuth:
            register_btn = self.Menu_Button(self, text="Создать профиль", command=self.register_user)
            register_btn.grid(row=3, column=1, sticky=ctk.EW)
            ###

            ###

            Login_btn = self.Menu_Button(self, text="Войти", command=self.register_user)
            Login_btn.grid(row=2, column=1, sticky=ctk.EW)

        else:
            self.name_label = ctk.CTkLabel(self, text=APP.User)
            self.name_label.grid(row=2, column=1)

    def register_user(self):
        if self.name_entry.get():
            self.APP.register_user(self.name_entry.get())
            self.APP.change_main_frame("profile")
