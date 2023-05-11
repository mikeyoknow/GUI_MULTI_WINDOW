import tkinter as tk

class FirstWindow:
    def __init__(self, master):
        self.master = master
        master.title("First Window")

        self.button = tk.Button(master, text="Open Second Window", command=self.open_second_window)
        self.button.pack()

    def open_second_window(self):
        self.master.destroy()  # close the first window
        second_window = tk.Tk()
        SecondWindow(second_window)

class SecondWindow:
    def __init__(self, master):
        self.master = master
        master.title("Second Window")

        self.label = tk.Label(master, text="This is the second window.")
        self.label.pack()

        self.button = tk.Button(master, text="submit", command=self.open_third_window)
        self.button.pack()

    def open_third_window(self):
        self.master.destroy()  # close the first window
        third_window = tk.Tk()
        ThirdWindow(third_window)

class ThirdWindow:
    def __init__(self, master):
        self.master = master
        master.title("Rotaion - press 'next'")


root = tk.Tk()
FirstWindow(root)
root.mainloop()
