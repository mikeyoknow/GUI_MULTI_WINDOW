# GUI_MULTI_WINDOW
In here, I will try to make my first multi window GUI in python
Later, I learned that I can use this newly unlocked skill to create a rotation system for my workplace

# What I've learned:
- The code is written in Python using the Tkinter library for building graphical user interfaces (GUI).
- The code defines three classes: FirstWindow, NameWindow, and DisplayWindow, which represent different windows or screens in the application.
The FirstWindow class is a subclass of tk.Tk, which represents the main application window. It initializes the window, sets its title and geometry, and creates various widgets such as labels, entry fields, and a submit button.
- The dataCollection method of the FirstWindow class is triggered when the submit button is clicked. It retrieves the number of staff working today from the entry field, checks if the value is a positive integer, and if so, hides the current window and opens the NameWindow to collect names.
- The NameWindow class is a subclass of tk.Toplevel, which represents a separate window that appears above the main window. It is created when the submit button in the FirstWindow is clicked. It sets the title and geometry of the window and dynamically creates labels and entry fields based on the number of staff provided. It also has a submit button to trigger the display_names method.
- The display_names method of the NameWindow class retrieves the names entered in the entry fields, destroys the current window, and opens the DisplayWindow to display the names.
- The DisplayWindow class is another subclass of tk.Toplevel created when the display_names method is triggered. It displays the names one by one in a label and provides a "Next" button to cycle through the names.
- The code uses the mainloop method to start the event loop, which listens for user interactions and updates the GUI accordingly.
- The if __name__ == "__main__": condition ensures that the code block following it is executed only when the script is run directly, not when it is imported as a module
