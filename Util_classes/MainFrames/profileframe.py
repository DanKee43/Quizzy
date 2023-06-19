
from Util_classes.MainFrames.MainFrameBase import MainFrameBase, ctk


class ProfileFrame(MainFrameBase):
    def __init__(self, APP):
        super().__init__(APP)
        self.APP = APP  # Reference to App instance
        self.fg_color, self.fg_color_hover = APP.get_main_colors()
        self.btn_font = ("Arial", 20, "bold")

        if not APP.IsAuth:
            self.NextPage = None
            register_btn = self.Menu_Button(self, text="Создать профиль",
                                            command=lambda page="registration": self.APP.change_main_frame(page))
            register_btn.grid(row=3, column=1, sticky=ctk.EW)

            Login_btn = self.Menu_Button(self, text="Войти",
                                         command=lambda page="login": self.APP.change_main_frame(page))
            Login_btn.grid(row=2, column=1, sticky=ctk.EW)

        else:
            name_label = ctk.CTkLabel(self, text=APP.User.get_username(),
                                      font=self.btn_font, fg_color="gray")
            name_label.grid(row=2, column=1)

            online_label = ctk.CTkLabel(self, text=APP.IsOnline,
                                        font=self.btn_font, fg_color="gray")
            online_label.grid(row=3, column=1)




class RegistrationPage(MainFrameBase):
    def __init__(self, APP):
        super().__init__(APP)

        Frame = ctk.CTkFrame(self, )

        name_label = ctk.CTkLabel(self, text="Введите имя:")
        name_label.grid(row=2, column=1)
        name_entry = ctk.CTkEntry(self, placeholder_text="От 5 до 15 символов")
        name_entry.grid(row=3, column=1)

        pass_label = ctk.CTkLabel(self, text="Введите пароль:")
        pass_label.grid(row=4, column=1)
        pass_entry = ctk.CTkEntry(self, placeholder_text="")
        pass_entry.grid(row=5, column=1)

        # register_btn = self.Menu_Button()


class LoginPage(MainFrameBase):
    def __init__(self, master):
        super().__init__(master)

        aboba2 = ctk.CTkLabel(self, text="LOGIN YOP", font=("", 50), fg_color="yellow")
        aboba2.pack()
