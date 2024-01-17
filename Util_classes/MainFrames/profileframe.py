from Util_classes.MainFrames.MainFrameTemplate import MainFrameTemplate, ctk


class ProfileFrame(MainFrameTemplate):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.fg_color, self.fg_color_hover = main_window.get_main_colors()
        self.btn_font = ("Arial", 20, "bold")

        if not main_window.App_Controller.
            print(main_window.App_Controller._User._Username)



class RegistrationPage(MainFrameTemplate):
    def __init__(self, APP):
        super().__init__(APP)

        name_label = ctk.CTkLabel(self, text="Введите имя:")
        name_label.grid(row=2, column=1)
        name_entry = ctk.CTkEntry(self, placeholder_text="От 5 до 15 символов")
        name_entry.grid(row=3, column=1)

        pass_label = ctk.CTkLabel(self, text="Введите пароль:")
        pass_label.grid(row=4, column=1)
        pass_entry = ctk.CTkEntry(self, placeholder_text="")
        pass_entry.grid(row=5, column=1)

        # register_btn = self.Menu_Button()


class LoginPage(MainFrameTemplate):
    def __init__(self, master):
        super().__init__(master)

        aboba2 = ctk.CTkLabel(self, text="LOGIN YOP", font=("", 50), fg_color="yellow")
        aboba2.pack()
