import tkinter as tk

class MyGUI:
    ''' Sample class to test the tkinter window '''
    
    def __init__(self):
        
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.geometry("500x500+200+200")
        
        # Create radio button with integer variable
        self.radio_var = tk.IntVar()
        self.rbutton_1 = tk.Radiobutton(self.main_window,
                                        text = "Radio Button 1",
                                        variable = self.radio_var,
                                        value = 1,
                                        command = self.disp_selection)
        
        self.rbutton_2 = tk.Radiobutton(self.main_window,
                                        text = "Radio Button 2",
                                        variable = self.radio_var,
                                        value = 2,
                                        command = self.disp_selection)
        
        self.rbutton_3 = tk.Radiobutton(self.main_window,
                                        text = "Radio Button 3",
                                        variable = self.radio_var,
                                        value = 3,
                                        command = self.disp_selection)
        
        # Create a label to display output message
        self.disp_msg = tk.StringVar()
        self.msg_output = tk.Label(self.main_window,
                                   width = 30,
                                   textvariable = self.disp_msg)
        
        # Pack widgets into window
        self.rbutton_1.pack(side = "top")
        self.rbutton_2.pack(side = "top")
        self.rbutton_3.pack(side = "top")
        self.msg_output.pack(side = "top")
        
        # Start the window event loop
        self.main_window.mainloop()
        
    # Callback function for radio button
    def disp_selection(self):
        self.disp_msg.set("You selected option " + str(self.radio_var.get()))
        
        
if __name__ == "__main__":
    my_gui = MyGUI()
        