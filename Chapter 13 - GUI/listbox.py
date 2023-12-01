import tkinter as tk

class MyGUI:
    ''' Sample class to test the tkinter window '''
    
    def __init__(self):
        
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.geometry("500x500+200+200")
        
        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self.main_window,
                                      orient = tk.VERTICAL)
        
        # Create a list box with vertical scrollbar
        self.listbox = tk.Listbox(self.main_window,
                                  yscrollcommand = self.scrollbar.set)
        
        # Add items to the list box
        for item in range(1,100):
            self.listbox.insert(tk.END, item)
            
        # Pack the list box and scrollbar
        self.scrollbar.pack(side = "right", fill = tk.Y)
        self.listbox.pack(side = "left", fill = tk.BOTH, expand = 1)
        
        # Start the window event loop
        self.main_window.mainloop()
        
if __name__ == "__main__":
    my_gui = MyGUI()