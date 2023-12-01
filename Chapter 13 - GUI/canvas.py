import tkinter as tk
import tkinter.font

class my_Gui:
    ''' Simple class to test the tkinter module '''
    def __init__(self):
        
        # Create the main window
        self.main_window = tk.Tk()
        
        # Size the window
        self.main_window.geometry("500x500+200+200")

        # Create a canvas sandbox
        self.canvas = tk.Canvas(self.main_window, 
                                bg = "tan", 
                                cursor = "mouse")
        
        # Create a line
        self.canvas.create_line(0, 0, 50, 50, width=5)
        
        # Create a rectangle
        self.canvas.create_rectangle(50, 50, 80, 70, 
                                     dash = (5,2), width = 3,
                                     outline = "red")
        
        # Create an oval
        self.canvas.create_oval(90, 50, 140, 80, 
                                fill = "blue", width = 3)
        
        # Create an arc
        self.canvas.create_arc(150, 50, 200, 80, 
                               start = 180, extent = 90, 
                               fill = "green", outline = "black")
        
        # Create a polygon
        self.canvas.create_polygon(210, 50, 230, 80, 260, 80, 
                                   280, 50, 245, 60, 
                                   fill = "yellow", outline = "black")
        
        fontToUse = tk.font.Font(family = "Helvetica", 
                                 size = 14, 
                                 weight = "bold",
                                 underline = 1)
        
        self.canvas.create_text(150, 100,
                                 text = "See all the graphics I can draw!",
                                 font = fontToUse)
        
        # Pack the canvas and fill the frame
        self.canvas.pack(side = "left", fill = tk.BOTH, expand = 1)
        
        # Display some canvas statistics
        print("Requested width = ", self.canvas.winfo_reqwidth())
        print("Screen width = ", self.canvas.winfo_screenwidth())
        print("Requested height = ", self.canvas.winfo_reqheight())
        print("Screen height = ", self.canvas.winfo_screenheight())
                
        # Start the window event loop
        self.main_window.mainloop()
        

if __name__ == '__main__':
    my_gui = my_Gui()