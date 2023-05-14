import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Rotation")

        # Set the window size
        self.root.geometry("600x480")

        # Change the background color
        self.root.configure(bg="#f0f0f0")

        # Initial Variables
        self.staff_list = []
        self.current_index = 0

        # Create left and right frames
        self.left_frame = ttk.Frame(self.root)
        self.right_frame = ttk.Frame(self.root)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Listbox to display staff names
        self.staff_display = tk.Listbox(self.left_frame, font=("Arial", 12))
        self.staff_display.pack(pady=20)

        # Entry field and button to add staff names
        self.name_entry = ttk.Entry(self.left_frame, font=("Arial", 12))
        self.name_entry.pack(pady=10)
        self.add_button = ttk.Button(self.left_frame, text="Add Staff", command=self.add_staff)
        self.add_button.pack(pady=10)

        # Buttons to indicate staff going for lunch and returning
        self.lunch_button = ttk.Button(self.left_frame, text="Go to Lunch", command=self.go_to_lunch)
        self.lunch_button.pack(pady=10)
        self.back_button = ttk.Button(self.left_frame, text="Back from Lunch", command=self.back_from_lunch)
        self.back_button.pack(pady=10)

        # Button to delete selected staff name
        self.del_button = ttk.Button(self.left_frame, text="Delete Selected", command=self.del_staff)
        self.del_button.pack(pady=10)

        # Buttons to move staff up and down
        self.up_button = ttk.Button(self.left_frame, text="Move Up", command=self.move_up)
        self.up_button.pack(pady=10)
        self.down_button = ttk.Button(self.left_frame, text="Move Down", command=self.move_down)
        self.down_button.pack(pady=10)

        # Label to display rotation
        self.rotation_display = ttk.Label(self.right_frame, text="", font=("Arial", 24, "bold"))
        self.rotation_display.pack(pady=20)

        # Button to rotate staff names
        self.next_button = ttk.Button(self.right_frame, text="Next", command=self.next_staff)
        self.next_button.pack(pady=200)

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
            self.staff_list[index], self.staff_list[index - 1] = self.staff_list[index - 1], self.staff_list[index]
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

    def update_rotation_display(self):
        if self.staff_list:
            # Set the new text with a large and bold font
            self.rotation_display.config(text=self.staff_list[self.current_index], font=("Arial", 24, "bold"))
        else:
            self.rotation_display.config(text="")

    def go_to_lunch(self):
        selected_name = self.staff_display.curselection()
        if selected_name:
            index = selected_name[0]
            if not self.staff_list[index].endswith("(On Lunch)"):
                self.staff_list[index] += " (On Lunch)"
                self.staff_display.delete(index)
                self.staff_display.insert(index, self.staff_list[index])
                self.staff_display.select_set(index)
                self.update_rotation_display()

    def back_from_lunch(self):
        selected_name = self.staff_display.curselection()
        if selected_name:
            index = selected_name[0]
            if self.staff_list[index].endswith("(On Lunch)"):
                self.staff_list[index] = self.staff_list[index][:-10]  # Remove " (On Lunch)"
                self.staff_display.delete(index)
                self.staff_display.insert(index, self.staff_list[index])
                self.staff_display.select_set(index)
                self.update_rotation_display()
            
root = tk.Tk()
app = RotationApp(root)
root.mainloop()