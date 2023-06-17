import customtkinter as ctk
from PIL import Image


class SideBarMenu(ctk.CTkFrame):
    def __init__(self, APP):
        super().__init__(APP)
        self.APP = APP
        self.configure(corner_radius=4, border_width=2, border_color="black", fg_color=APP.get_main_colors()[0],
                       width=50)
        self.path = "static/sidebar/"
        self.buttons_list = ["menu", "profile", "friends", "stats", "settings"]
        self.btn_objs_list = []
        self.btn_size = 40

        self.btn_count = 0

        for btn_name in self.buttons_list:
            self.add_btn(btn_name)

    def add_btn(self, btn_name):
        curr_btn_logo_pic = ctk.CTkImage(Image.open(f"{self.path}{btn_name}.png"),
                                         size=(self.btn_size, self.btn_size), )

        curr_btn = ctk.CTkButton(self, image=curr_btn_logo_pic, text="",
                                 fg_color="transparent", width=self.btn_size, height=self.btn_size,
                                 hover_color=self.APP.get_main_colors()[1],
                                 command=lambda frame_name=btn_name: self.APP.change_main_frame(frame_name))


        self.btn_objs_list.append(curr_btn)
        curr_btn.grid(row=self.btn_count, pady=5, padx=5)
        self.btn_count += 1
