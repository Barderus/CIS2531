import tkinter as tk

class MyGUI:
    ''' sample class to test the tkinter window '''
    
    def __init__(self):
        
        # Create the main window
        self.main_window = tk.Tk()
        
        # Create some labels for placement
        self.tl1 = tk.Label(self.main_window, text= "Label 1")
        self.tl2 = tk.Label(self.main_window, text= " Label 2")
        
        '''
        # Using pack method for container placement
        self.tl1.pack(side = "top")
        self.tl2.pack(side = 'top')
        '''
        
        '''
        # Using grid method for container placement
        self.tl1.grid(row = 0, column = 0)
        self.tl2.grid(row = 0, column=1)
        '''
        
        # Using place method for container placement
        self.tl1.place(relx = .1, rely = .1, anchor="nw")
        self.tl2.place(relx = .5, rely = .5, anchor= "center")
        
        # Start the window event loop
        self.main_window.mainloop()
        
if __name__ == "__main__":
    my_gui = MyGUI()