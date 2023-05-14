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
        self.add_button = tk.Button(self.left_frame, text="Add Staff", command=self.add_staff)
        self.add_button.pack()
        
        #Buttons to delete names
        self.del_button = tk.Button(self.left_frame, text="Delete Selected", command=self.del_staff)
        self.del_button.pack()

        #Buttons to move staff up and down
        self.up_button = tk.Button(self.left_frame, text="Move up", command=self.move_up)
        self.up_button.pack()
        self.down_button = tk.Button(self.left_frame, text="Move down", command=self.move_down)
        self.down_button.pack()

        #Label to display rotation
        self.rotation_display = tk.Button(self.right_frame, text="")
        self.rotation_display.pack(pady=20)

        #Button to rotate staff names
        self.next_button = tk.Button(self.right_frame, text="Next", command=self.next_staff)
        self.next_button.pack(pady=100)

    def add_staff(self):
        new_name = self.name_entry.get()
        if new_name:
            self.staff_list.append(new_name)
            self.staff_display.insert("end", new_name)
            self.name_entry.delete(0, "end")
            self.update_rotation_display()

    def del_staff(self):
        selected_name = self.staff_display.curselection()
        if selected_name:
            self.staff_list.pop(selected_name[0])
            self.staff_display.delete(selected_name)
            self.update_rotation_display()

    def next_staff(self):
        if self.staff_list:
            self.current_index = (self.current_index + 1) % len(self.staff_list)
            self.update_rotation_display()

    def move_up(self):
        selected_name = self.staff_display.curselection()
        if selected_name and selected_name[0] > 0:
            index = selected_name[0]
            self.staff[index], self.staff_list[index - 1] = self.staff_list[index - 1], self.staff_list[index]
            self.staff_display.delete(index)
            self.staff_display.insert(index - 1, self.staff_list[index - 1])
            self.staff_display.select_set(index - 1)
            self.update_rotation_display()
    
    def move_down(self):
        selected_name = self.staff_display.curselection()
        if selected_name and selected_name[0] < len(self.staff_list) - 1:
            index = selected_name[0]
            self.staff_list[index], self.staff_list[index + 1] = self.staff_list[index + 1], self.staff_list[index]
            self.staff_display.delete(index)
            self.staff_display.insert(index + 1, self.staff_list[index + 1])
            self.staff_display.select

root = tk.Tk()
app = RotationApp(root)
root.mainloop()