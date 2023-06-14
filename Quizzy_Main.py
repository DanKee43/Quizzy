from tkinter import *
import requests
import threading
from PIL import Image
import customtkinter as ctk
import tracemalloc

Window_Width = 1500
Window_Height = 900

ctk.set_default_color_theme("static/green.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QUIZZY")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (Window_Width / 2)
        y = (screen_height / 2) - (Window_Height / 2)
        self.geometry('%dx%d+%d+%d' % (int(Window_Width*0.6), int(Window_Height*0.6), x, y))
        self.minsize(int(Window_Width*0.6), int(Window_Height*0.6))
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=29)


        self.Main_header = MainHeader(self)
        # self.Main_header.pack(side=TOP, fill=X)
        self.Main_header.grid(row=0, columnspan=2, sticky=NSEW)

        self.Left_frame = ctk.CTkFrame(self, fg_color="#292929")
        self.labbel = ctk.CTkLabel(self.Left_frame, text="TEST\nOptions\nMenu", font=("", 30), text_color="green").pack()
        self.Left_frame.configure(corner_radius=0)
        self.Left_frame.grid(row=1, column=0, sticky=NSEW)




        # Создаем два фрейма между которыми будем переключаться
        self.Main_frame = MainFrame(self)
        self.Game_Frame = InGameFrame(self)
        # self.INET = ctk.CTkLabel(self, text="ИНЕТ ЕСТЬ", text_color="green", font=("", 22))
        # self.INET.pack(side=BOTTOM)
        # self.check_connection()

        self.Main_frame.grid(row=1, column=1, sticky=NSEW)

    # def check_connection(self):
    #     try:
    #         requests.head("http://www.google.com/", timeout=0.5)
    #         self.INET.configure(text="ИНЕТ ЕСТЬ", text_color="green")
    #         print("kaif")
    #     except requests.ConnectionError:
    #         self.INET.configure(text="ИНЕТА НЕМА", text_color="red")
    #         print("The internet connection is down")
    #     threading.Timer(3, self.check_connection).start()



class MainHeader(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#FFA302", bg_color="#FFA302")
        self.App_obj = master
        # self.columnconfigure(0, weight=1)
        # self.Logo = ctk.CTkLabel(self, text="QUIZZY", font=("", 33))
        # self.Logo.pack(side=LEFT)
        self.LOGO_PICK = ctk.CTkImage(Image.open("QUIZZY.png"), size=(200, 50))
        self.Logo = ctk.CTkLabel(self, image=self.LOGO_PICK, text="", fg_color="red")
        self.Logo.pack(side=LEFT)



class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.App_obj = master
        self.configure(fg_color="#7A7A7A")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.lab1 = ctk.CTkLabel(self, text="WINDOW1", bg_color="#FFA302", font=("", 50))
        self.lab1.grid(row=0)
        self.btn1 = ctk.CTkButton(self, text="change_window", command=self.win12)
        self.btn1.grid(row=1)

    def win12(self):
        print("frame1")
        self.App_obj.Main_frame.grid_forget()
        print(tracemalloc.get_traced_memory())
        self.App_obj.Game_Frame.grid(row=1, column=1, sticky=NSEW)



class InGameFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, **kwargs):
        super().__init__(master, **kwargs)
        self.App_obj = master
        self.configure(fg_color="#7A7A7A")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        lab2 = ctk.CTkLabel(self, text="WINDOW2", bg_color="#00E8FC", font=("", 50))
        lab2.grid(row=0)
        btn2 = ctk.CTkButton(self, text="change_window", command=self.win21)
        btn2.grid(row=1)

    def win21(self):
        print("frame2")
        self.App_obj.Game_Frame.grid_forget()
        print(tracemalloc.get_traced_memory())
        self.App_obj.Main_frame.grid(row=1, column=1, sticky=NSEW)



if __name__ == "__main__":
    tracemalloc.start()
    app = App()
    print(tracemalloc.get_traced_memory())
    app.mainloop()
