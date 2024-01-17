from Util_classes.MainFrames.MainFrameTemplate import MainFrameTemplate, ctk
from PIL import Image


class MainMenu(MainFrameTemplate):
    def __init__(self, APP):
        super().__init__(APP)  # Reference to App instance
        self.fg_color, self.fg_color_hover = APP.get_main_colors()
        self.btn_font = ("Arial", 26, "bold")

        self.APP = APP

        self.scene_1, self.scene_2, self.scene_2_1, self.scene_2_2 = [], [], [], []
        self.scenes_map = {"scene_1": self.scene_1, "scene_2": self.scene_2,
                           "scene_2_1": self.scene_2_1, "scene_2_2": self.scene_2_2}

        self.current_scene = "scene_1"
        self.previous_scene = ""

        BACK_btn = ctk.CTkButton(self, image=ctk.CTkImage(Image.open("static/left_arrow.png"), size=(30, 30)),
                                 text="", width=30, height=30, fg_color="transparent", hover=False,
                                 command=lambda scene="BACK": self.change_scene(scene))
        BACK_btn.grid(row=0, column=0, sticky=ctk.NW, pady=5, padx=5)

        # ------------------------------------------------------------------------------------------------# scene_1

        PLAY_btn = self.MenuButton(self, text="Играть",
                                   command=lambda scene="scene_2": self.change_scene(scene))
        PLAY_btn.grid(row=1, column=1, pady=(50, 0), sticky=ctk.EW)

        EXIT_btn = self.MenuButton(self, text="Выйти",
                                   command=lambda root=APP: APP.destroy())
        EXIT_btn.grid(row=9, column=1, pady=10, sticky=ctk.EW)

        self.scene_1.append(PLAY_btn)
        self.scene_1.append(EXIT_btn)

        # ------------------------------------------------------------------------------------------------# scene_2

        # if not self.APP.IsAuth:
        #     not_auth_label = ctk.CTkLabel(self, text="Вы не авторизованы!", text_color="red",
        #                                   font=self.btn_font)
        #     not_auth_label.grid(row=0, column=1)
        #     not_auth_label.grid_remove()
        #     self.scene_2.append(not_auth_label)

        CONNECT_btn = self.MenuButton(self, text="Подключиться к игре",
                                      command=lambda scene="scene_2_1": self.join_game(scene))
        CONNECT_btn.grid(row=1, column=1, pady=(50, 0), sticky=ctk.EW)
        CONNECT_btn.grid_remove()

        CREATE_ROOM_btn = self.MenuButton(self, text="Создать игру",
                                          command=lambda scene="scene_2_2": self.join_game(scene))
        CREATE_ROOM_btn.grid(row=2, column=1, pady=10, sticky=ctk.EW)
        CREATE_ROOM_btn.grid_remove()

        self.scene_2.append(CONNECT_btn)
        self.scene_2.append(CREATE_ROOM_btn)

        # --------------------------------------------------------------# scene_2_1 (Join game)

        INPUT_ID_label = ctk.CTkLabel(self, text="Введите ID комнаты", font=self.btn_font)
        INPUT_ID_label.grid(row=1, column=1, pady=(50, 0), sticky=ctk.EW)
        INPUT_ID_label.grid_remove()

        INPUT_ID_entry = ctk.CTkEntry(self, font=self.btn_font, corner_radius=4)
        INPUT_ID_entry.grid(row=2, column=1, pady=10, sticky=ctk.EW)
        INPUT_ID_entry.grid_remove()

        JOIN_btn = self.MenuButton(self, text="Подключиться",
                                   command=lambda frame_name="Game_frame": APP.change_main_frame(frame_name))
        JOIN_btn.grid(row=3, column=1, pady=10, sticky=ctk.EW)
        JOIN_btn.grid_remove()

        self.scene_2_1.append(INPUT_ID_label)
        self.scene_2_1.append(INPUT_ID_entry)
        self.scene_2_1.append(JOIN_btn)

        # --------------------------------------------------------------# scene_2_2 (create game)

        CREATE_GAME_btn = self.MenuButton(self, text="Создать игру")
        CREATE_GAME_btn.grid(row=3, column=1, sticky=ctk.EW)
        CREATE_GAME_btn.grid_remove()

        self.scene_2_2.append(CREATE_GAME_btn)

    def change_scene(self, destination: str):
        if destination == "BACK":
            destination = self.previous_scene

        if destination:
            for widget in self.scenes_map.get(self.current_scene):
                widget.grid_remove()
            for widget in self.scenes_map.get(destination):
                widget.grid()

            self.previous_scene = self.current_scene
            self.current_scene = destination
