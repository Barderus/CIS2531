import tkinter as tk

class MyGUI:
    ''' Sample class to test the tkinter window '''
    
    def __init__(self):
        
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.geometry("500x500+200+200")
        
        # Create a check button with integer variable
        self.check_var = tk.IntVar()
        self.check_button = tk.Checkbutton(self.main_window, 
                                           text="Check button", 
                                           variable=self.check_var,
                                           command = self.disp_selection)
        
        #  Create a label to display the selection
        self.disp_msg = tk.StringVar()
        self.msg_output = tk.Label(self.main_window,
                                   width = 30, 
                                   textvariable=self.disp_msg)
        
        # Se initial check button status
        self.check_button.deselect()
        self.disp_selection()
        
        # Pack the widgets
        self.check_button.pack(side = "top")
        self.msg_output.pack(side = "top")
        
        # Start the window event loop
        self.main_window.mainloop()

    def disp_selection(self):
        self.disp_msg.set("Check button status: " + str(self.check_var.get()))

if __name__ == "__main__":
    my_gui = MyGUI()