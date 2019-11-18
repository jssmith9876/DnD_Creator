from interface import Application
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()

    app = Application(master=root)
    app.master.title("DnD Character Creator")
    # app.master.maxsize(1000, 400)
    app.mainloop()