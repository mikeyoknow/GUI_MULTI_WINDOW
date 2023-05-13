import tkinter as tk
from tkinter import messagebox

class RotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Rotation")

        #Initial Variables
        self.staff_list = []
        self.current_index = 0

        #Create left and right frame panels
        self.left_frame = tk.Frame(self.root)
        self.right_frame = tk.Frame(self.root)
        self.left_frame.pack(side="left", fill="both", expand=True)
        self.right_frame.pack(side="right", fill="both", expand=True)

        #Listbox to displat staff name
        self.staff_display = tk.Listbox(self.left_frame)
        self.staff_display.pack(pady=20)

        #Entry field and button to add staff names
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.pack()
