# import tkinter
from memory_profiler import profile
from PIL import Image
import customtkinter as ctk
import tracemalloc

Window_Width = 1500
Window_Height = 900


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QUIZZY")
        self.configure(fg_color="#D0D0D0")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (Window_Width / 2)
        y = (screen_height / 2) - (Window_Height / 2)
        self.geometry('%dx%d+%d+%d' % (int(Window_Width * 0.6), int(Window_Height * 0.6), x, y))
        self.minsize(int(Window_Width * 0.6), int(Window_Height * 0.6))
        # self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)
        # self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=29)

        self.main_color = "#FFA302"
        self.main_color_hover = "#E18502"

        self.Main_header = MainHeader(self)
        self.Main_header.grid(row=0, columnspan=2, sticky=ctk.NSEW)

        self.Side_Menu = SideBarMenu(self)
        self.Side_Menu.grid(row=1, pady=(5, 0), padx=(0, 5), column=0, sticky=ctk.NSEW)

        self.Main_frame = MainMenu(self)
        self.Main_frame.grid(row=1, pady=(5, 0), padx=0, column=1, sticky=ctk.NSEW)

    def get_main_colors(self):
        return self.main_color, self.main_color_hover

    def change_main_frame(self, frame_name):
        pass

    def change_main_color(self):
        pass


class MainHeader(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=master.get_main_colors()[0], corner_radius=0)
        self.LOGO_PICK = ctk.CTkImage(Image.open("static/QUIZZY.png"), size=(200, 50))
        self.Logo = ctk.CTkLabel(self, image=self.LOGO_PICK, text="", fg_color="transparent")
        self.Logo.grid(pady=(10, 10))


class SideBarMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=4, border_width=2, border_color="black", fg_color=master.get_main_colors()[0],
                       width=50)
        self.path = "static/sidebar/"
        self.buttons_list = ["profile", "friends", "stats", "settings"]
        self.btn_objs_list = []
        self.btn_size = 45

        self.btn_count = 0

        for btn_name in self.buttons_list:
            self.add_btn(btn_name)

    def add_btn(self, btn_name):
        curr_btn_logo_pic = ctk.CTkImage(Image.open(f"{self.path}{btn_name}.png"),
                                         size=(self.btn_size, self.btn_size), )

        curr_btn = ctk.CTkButton(self, image=curr_btn_logo_pic, text="",
                                 fg_color="transparent", width=self.btn_size, height=self.btn_size)

        self.btn_objs_list.append(curr_btn)
        curr_btn.grid(row=self.btn_count, pady=5, padx=5)
        self.btn_count += 1


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=4, border_width=2,
                       border_color="black", fg_color="#CECECE")


class MainMenu(MainFrame):
    class Menu_Button(ctk.CTkButton):
        def __init__(self, master, text, color, hover_color, command=None):
            super().__init__(master)
            self.configure(text=text, text_color="black", font=master.btn_font,
                           fg_color=color, hover_color=hover_color,
                           corner_radius=6, border_width=2, border_color="black",
                           command=command)

    def __init__(self, master):
        super().__init__(master)
        self.fg_color, self.fg_color_hover = master.get_main_colors()
        self.btn_font = ("Arial", 26, "bold")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        for i in range(10):
            self.rowconfigure(i, weight=1)

        self.scene_1, self.scene_2, self.scene_2_1, self.scene_2_2 = [], [], [], []
        self.scenes_map = {"scene_1": self.scene_1, "scene_2": self.scene_2,
                           "scene_2_1": self.scene_2_1, "scene_2_2": self.scene_2_2}
        self.current_scene = "scene_1"
        self.previous_scene = ""


        # ------------------------------------------------------------------------------------------------# scene_1

        self.PLAY_btn = self.Menu_Button(self, text="Играть", color=self.fg_color, hover_color=self.fg_color_hover,
                                         command=lambda scene="scene_2": self.change_scene(scene))
        self.PLAY_btn.grid(row=1, column=1, pady=(50, 0), sticky=ctk.EW)

        self.EXIT_btn = self.Menu_Button(self, text="Выйти", color=self.fg_color, hover_color=self.fg_color_hover,
                                         command=lambda root=master: master.destroy())
        self.EXIT_btn.grid(row=9, column=1, pady=10, sticky=ctk.EW)

        self.scene_1.append(self.PLAY_btn)
        self.scene_1.append(self.EXIT_btn)

        # ------------------------------------------------------------------------------------------------# scene_2

        self.CONNECT_btn = self.Menu_Button(self, text="Подключиться к игре",
                                            color=self.fg_color, hover_color=self.fg_color_hover,
                                            command=lambda scene="scene_1": self.change_scene(scene))
        self.CONNECT_btn.grid(row=1, column=1, pady=(50, 0), sticky=ctk.EW)
        self.CONNECT_btn.grid_remove()

        self.CREATE_ROOM_btn = self.Menu_Button(self, text="Создать игру",
                                                color=self.fg_color, hover_color=self.fg_color_hover)
        self.CREATE_ROOM_btn.grid(row=2, column=1, pady=10, sticky=ctk.EW)
        self.CREATE_ROOM_btn.grid_remove()

        self.scene_2.append(self.CONNECT_btn)
        self.scene_2.append(self.CREATE_ROOM_btn)

        # ------------------------------------------------------------------------------------------------#

    def change_scene(self, destination: str):
        for widget in self.scenes_map.get(self.current_scene):
            widget.grid_remove()
        for widget in self.scenes_map.get(destination):
            widget.grid()

        self.previous_scene = self.current_scene
        self.current_scene = destination




# class MainFrame(ctk.CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.App_obj = master
#         self.configure(fg_color="#D3D3D3", border_width=2, border_color="black",)
#         # self.rowconfigure(0, weight=1)
#         # self.rowconfigure(1, weight=1)
#
#         self.lab1 = ctk.CTkLabel(self, text="WINDOW1", bg_color="#A8A8A8", font=("", 50))
#         self.lab1.place(x=10, y=10)
#         self.btn1 = ctk.CTkButton(self, text="change_window", command=self.win12)
#         self.btn1.place(x=10, y=100)
#
#     @profile
#     def win12(self):
#         # print("frame1")
#         self.App_obj.Main_frame.grid_forget()
#         # self.App_obj.Left_fra
#         # self.App_obj.columnconfigure(0, weight=6)
#         # print(tracemalloc.get_traced_memory())
#         self.App_obj.Game_Frame.grid(row=1, pady=(5, 0), padx=0, column=1, sticky=NSEW)
#


# class InGameFrame(ctk.CTkFrame):
#     def __init__(self, master: ctk.CTk, **kwargs):
#         super().__init__(master, **kwargs)
#         self.App_obj = master
#         self.configure(fg_color="#F5F5F5")
#         # self.rowconfigure(0, weight=1)
#         # self.rowconfigure(1, weight=1)
#         lab2 = ctk.CTkLabel(self, text="WINDOW2", bg_color="#00E8FC", font=("", 50))
#         lab2.grid(row=1, column=1)
#         btn2 = ctk.CTkButton(self, text="change_window", command=self.win21)
#         btn2.grid(row=2, column=1)
#
#     @profile
#     def win21(self):
#         # print("frame2")
#         self.App_obj.Game_Frame.grid_forget()
#         # self.App_obj.columnconfigure(0, weight=1)
#         # print(tracemalloc.get_traced_memory())
#         self.App_obj.Main_frame.grid(row=1, pady=(5, 0), padx=0, column=1, sticky=NSEW)


if __name__ == "__main__":
    tracemalloc.start()
    app = App()
    # print(tracemalloc.get_traced_memory())
    app.mainloop()
