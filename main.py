import tkinter as tk

class FirstWindow(tk.Tk):
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
        self.submit.pack(pady=10)
        
    def dataCollection(self):
        try:
            num_people = int(self.entry_num.get())
            if num_people > 0:
                self.withdraw()
                name_input_window = NameWindow(self, num_people)
                name_input_window.grab_set()
        except ValueError:
            pass
class NameWindow(tk.Toplevel):
    def __init__(self, parent, num_people):
        super().__init__(parent)
        self.title("Enter Names")
        self.geometry("300x200")

        self.enteries = []
        self.labels = []
        for i in range(num_people):
            label = tk.Label(self, text=f"Person {i+1}:")
            label.grid(row=i, column=0)
            self.labels.append(label)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.enteries.append(entry)
        
        self.button_submit = tk.Button(self, text="Submit", command=self.display_names)
        self.button_submit.grid(row=num_people, column=1, pady=10)

    def display_names(self):
        names = [entry.get() for entry in self.enteries]
        self.destroy()
        display_window = DisplayWindow(self.master, names)
        display_window.grab_set()

class DisplayWindow(tk.Toplevel):
    def __init__(self, parent, names):
        super().__init__(parent)
        self.title("Names Display")
        self.geometry("300x200")

        self.names = names
        self.index = 0

        self.label = tk.Label(self, text=names[self.index])
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Next", command=self.next_name)
        self.button.pack(pady=10)
    def next_name(self):
        self.index = (self.index + 1) % len(self.names)
        self.label.config(text=self.names[self.index])

if __name__ == "__main__":
    First_Window = FirstWindow()
    First_Window.mainloop()
