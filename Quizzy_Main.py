from tkinter import *
import requests
import threading
from PIL import Image
import customtkinter as ctk
import tracemalloc

Window_Width = 1500
Window_Height = 900




class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("QUIZZY")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (Window_Width / 2)
        y = (screen_height / 2) - (Window_Height / 2)
        self.geometry('%dx%d+%d+%d' % (Window_Width, Window_Height, x, y))



        self.Main_header = MainHeader(self)
        self.Main_header.pack(side=TOP, fill=X)


        # Создаем два фрейма между которыми будем переключаться
        self.Main_frame = MainFrame(self)
        self.Game_Frame = InGameFrame(self)
        self.INET = ctk.CTkLabel(self, text="ИНЕТ ЕСТЬ", text_color="green", font=("", 22))
        self.INET.pack(side=BOTTOM)
        self.check_connection()
        # Упаковываем первый фрейм
        self.Main_frame.pack()

    def check_connection(self):
        try:
            requests.head("http://www.google.com/", timeout=0.5)
            self.INET.configure(text="ИНЕТ ЕСТЬ", text_color="green")
            print("kaif")
        except requests.ConnectionError:
            self.INET.configure(text="ИНЕТА НЕМА", text_color="red")
            print("The internet connection is down")
        threading.Timer(3, self.check_connection).start()

    def __del__(self):
        threading.Lock()


class MainHeader(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#FFA302", width=Window_Width)

        self.Logo = ctk.CTkLabel(self, text="QUIZZY", font=("", 33))
        self.Logo.pack(side=LEFT)


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.App_obj = master
        self.lab1 = ctk.CTkLabel(self, text="WINDOW1", bg_color="#FFA302", font=("", 50))
        self.lab1.pack()
        self.btn1 = ctk.CTkButton(self, text="change_window", command=self.win12)
        self.btn1.pack()

    def win12(self):
        print("frame1")
        self.App_obj.Main_frame.pack_forget()  # скрываем текущий фрейм
        print(tracemalloc.get_traced_memory())
        self.App_obj.Game_Frame.pack()  # отображаем второй фрейм

    def __del__(self):
        print("frame1 destructed")


class InGameFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, **kwargs):
        super().__init__(master, **kwargs)
        self.App_obj = master
        lab2 = ctk.CTkLabel(self, text="WINDOW2", bg_color="#00E8FC", font=("", 50))
        lab2.pack()
        btn2 = ctk.CTkButton(self, text="change_window", command=self.win21)
        btn2.pack()

    def win21(self):
        print("frame2")
        self.App_obj.Game_Frame.pack_forget()  # скрываем текущий фрейм
        print(tracemalloc.get_traced_memory())
        self.App_obj.Main_frame.pack()  # отображаем первый фрейм

    def __del__(self):
        print("frame2 destructed")


if __name__ == "__main__":
    tracemalloc.start()
    app = App()
    print(tracemalloc.get_traced_memory())
    app.mainloop()
