import tkinter
import tkinter.messagebox

class my_GUI():
    
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        self.main_window.geometry("500x500+200+200")
        
        # Create a label with text
        self.topFrame = tkinter.Frame(self.main_window)
        self.text_label = tkinter.Label(self.topFrame,
                                        text = "Enter your name: ")
        
        # Create an entry field for input
        self.text_entry = tkinter.Entry(self.topFrame, width = 10,
                                        cursor = "plus")
        
        #Pack widgets into top frame
        self.text_label.pack(side = "left")
        self.text_entry.pack(side = "left")
        
        # Create an output label
        self.bottomFrame = tkinter.Frame(self.main_window)
        self.textValue = tkinter.StringVar()
        self.text_output = tkinter.Label(self.bottomFrame, width = 10,
                                         textvariable = self.textValue)
        
        # Create button
        self.disp_button = tkinter.Button(self.bottomFrame, text = "Display",
                                          command = self.disp_text)
        
        #Pack widgets into bttom frame
        self.disp_button.pack(side = "left")
        self.text_output.pack(side = "left")
        
        # Pack frame into window (default "top")
        self.topFrame.pack()
        self.bottomFrame.pack()
        
        self.main_window.mainloop()
        

    def disp_text(self):
        ''' Simple retrieval and re-display of user input '''
        self.textValue.set(self.text_entry.get())
        
        

if __name__ == "__main__":
    my_gui = my_GUI()