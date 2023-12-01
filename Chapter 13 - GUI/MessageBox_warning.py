import tkinter
import tkinter.messagebox

class my_GUI():
    
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #self.main_window.geometry("300x200+2000+20")
        
        # Display a button to display showinfo messagebox
        self.show_info_button = tkinter.Button(self.main_window,
                                          text = "showinfo", command=self.show_info)
        
        # Create a button to display showwarning message box
        self.show_warning_button = tkinter.Button(self.main_window,
                                            text = "showwarninig", command = self.show_warning)
        
        # Create a button to display showerror messagebox
        self.show_error_button = tkinter.Button( self.main_window,
                                          text = "showerror", command = self.show_error)
        
        # Create a button to display askquestion messagebox
        self.ask_question_button = tkinter.Button(self.main_window,
                                            text = "askquestion", command = self.ask_question)
        
        # Create a button to display askokcancel messagebox
        self.ask_okcancel_button = tkinter.Button( self.main_window,
                                            text = "askokcancel", command = self.ask_okcancel)
        
        # Create a button to display askyesno messagebox
        self.ask_yesno_button = tkinter.Button(self.main_window,
                                         text = "askyesno", command = self.ask_yesno)
        
        # Create a button to display askretrycancel messagebox
        self.ask_retrycancel_button = tkinter.Button(self.main_window,
                                               text = "askretrycancel", command = self.ask_retrycancel)

        # Pack buttons
        self.show_info_button.pack(side = "top")
        self.show_warning_button.pack(side = "top")
        self.show_error_button.pack(side = "top")
        self.ask_question_button.pack(side = "top")
        self.ask_okcancel_button.pack(side = "top")
        self.ask_yesno_button.pack(side = "top")
        self.ask_retrycancel_button.pack(side = "top")
      
        self.main_window.mainloop()
        
    def show_info(self):
        tkinter.messagebox.showinfo("MessageBoxes", "This is the show_info messagebox")
        
    def show_warning(self):
        tkinter.messagebox.showwarning("MessageBoxes", "This is the show_warning messagebox")
        
    def show_error(self):
        tkinter.messagebox.showerror("MessageBoxes", "This is the show_error messagebox")
        
    def ask_question(self):
        response = tkinter.messagebox.askquestion("MessageBoxes", "This is the ask_question messagebox")
        
        print(response)
    def ask_okcancel(self):
        response = tkinter.messagebox.askokcancel("MessageBoxes", "This is the ask_okcancel messagebox")
        
        print(response)
    def ask_yesno(self):
        response = tkinter.messagebox.askyesno("MessageBoxes", "This is the ask_yesno messagebox")
        
        print(response)
    def ask_retrycancel(self):
        response = tkinter.messagebox.askretrycancel("MessageBoxes", "This is the ask_retrycancel messagebox")
        
        print(response)
        
        

if __name__ == "__main__":
    gui = my_GUI()
        
        