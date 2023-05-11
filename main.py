import tkinter as tk

class FirstWindow:
    def __init__(self):
        super().__init__()
        self.title("Rotation System")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Welcome to Rotation 1.0!")
        self.label.pack(pady=10)

        self.label_num = tk.Label(self, text="Number of staff working today: ")
        self.label_num.pack()

        self.entry_num = tk.Entry(self)
        self.entry_num.pack()

        self.submit = tk.Button(self, text="Submit", command=self.dataCollection)

    def dataCollection(self):
        try:
            num_people = int(self.entry_num.get())
            if num_people > 0:
                self.withdraw()
                name_input_window = NameWindow(self, num_people)
                name_input_window.grab_set()
        except ValueError:
            pass

root = tk.Tk()
FirstWindow(root)
root.mainloop()
