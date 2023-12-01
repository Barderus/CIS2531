import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

class my_GUI():

    def __init__(self):

        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Menu GUI")

        # Size of the window
        self.main_window.geometry("500x500+200+200")
        
        # Create a menu bar at top of window
        self.menubar = tk.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        # Add file menu options
        self.file_menu  = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label = "Save",
                                   command = self.save_file)
        self.file_menu.add_command(label = "Exit",
                                   command = self.main_window.destroy)
        
        # Help menu option
        self.help_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Help", menu = self.help_menu)
        self.help_menu.add_command(label = "About",
                                   command = self.show_about)
        
        
        # Start with the window event loop
        self.main_window.mainloop()
    
    # Menu option functions
    def save_file(self):
        # Get filename
        file_name = tk.filedialog.asksaveasfilename(initialdir = "/",
                                                    filetypes = [("Text files", "*.txt"),
                                                                 ("All files",".*")],
                                                    title = "Select file",
                                                    defaultextension = ".txt") 
        # Check for empty string
        if len(file_name) != 0:
            # Open file
            self.file_var = open(file_name, "w")
            # Write to file
            self.file_var.write("Hello World\n")
            # Close file
            self.file_var.close()
            
    def show_about(self):
        tk.messagebox.showinfo("Help", "This is a GUI\n\nWritten by: Gabriel dos Reis\n\nDate: 2023")
            
if __name__ == "__main__":
    my_GUI()
