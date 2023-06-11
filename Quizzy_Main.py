import tkinter
import customtkinter as ctk


window = ctk.CTk()
window.geometry("600x600")

ctk.set_default_color_theme("blue")


def click():
    print("clicked")


frame = ctk.CTkFrame(window)

btn = ctk.CTkSegmentedButton(frame,  values=["Value 1", "Value 2", "Value 3"], command=click).pack()

frame.pack()


window.mainloop()
