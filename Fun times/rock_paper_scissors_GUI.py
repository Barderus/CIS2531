'''
Rock Paper Scissors using Tkinter
'''
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

class Game_GUI:
    ROCK_PATH = r"C:\Users\gabe_\OneDrive\Pictures\Coding\rock1.png"
    PAPER_PATH = r"C:\Users\gabe_\OneDrive\Pictures\Coding\paper1.png"
    SCISSORS_PATH = r"C:\Users\gabe_\OneDrive\Pictures\Coding\scissors1.png"
    
    def __init__(self):

            # Create the main window
            self.main_window = tk.Tk()
            self.main_window.title("Menu GUI")

            # Size of the window
            self.main_window.geometry("400x450+550+200")
            
            # Create the game header
            self.head_label = tk.Label(self.main_window, text = "Rock Paper Scissors Game", font = ("Helvetica", 16))
            self.head_label.grid(row = 0, column = 2, padx = 20, pady = 20)
            
            
            '''
                Beginning of the result frame
            '''
            
            # Frame that will display the user's choice and PC's choice. 
            # The frame should change every time the user choose their "weapon"
            self.resultFrame = tk.Frame(self.main_window)
            self.resultFrame.grid(row = 2, column = 0, columnspan = 3, rowspan = 3) # Packing the frame in the window
            
            # Create the contents to insert into the result frame
            self.user_choice_entry = tk.Entry(self.resultFrame, width= 15, cursor= "left_ptr") 
            self.user_choice_entry.insert(0, "Player Choice")
            self.user_choice_entry.configure(state= tk.DISABLED, disabledbackground= "white", disabledforeground= "black")

            self.vs_Label = tk.Label(self.resultFrame, text = "VS")
            self.pc_choice_entry = tk.Entry(self.resultFrame, width= 15, cursor= "left_ptr")
            self.pc_choice_entry.insert(0, "PC Choice")
            self.pc_choice_entry.configure(state= tk.DISABLED, disabledbackground= "white", disabledforeground= "black")
            
            # Pack the content into the result frame using .grid
            self.user_choice_entry.grid(row = 0, column= 0, padx = 10, pady = 10)
            self.vs_Label.grid(row = 0, column = 1, padx = 10, pady = 10)
            self.pc_choice_entry.grid(row = 0, column = 2, padx = 10, pady = 10)
            
            
            '''
                End of the result frame
            '''
            
            '''
                Beginning of the selection frame
            '''
            # Selection frame allows the user to select one of the following options: Rock, Paper, or Scissors
            # Using buttons for the selection. Using confirmation before selection?
            self.selectionFrame = tk.Frame(self.main_window)
            self.selectionFrame.grid(row = 5, column = 2, rowspan= 3, columnspan= 3) # Packing the frame in the window
            
            '''
            # Creating a photoimage object to use iage
            rock_photo = tk.PhotoImage(file = r"rock1.png")
            paper_photo = tk.PhotoImage(file = r"paper1.png")
            scissors_photo = tk.PhotoImage(file= r"rock1.png")
            '''
            
            # Creation of content for selectionFrame
            self.choose_label = tk.Label(self.selectionFrame, text = "Choose:", font = ("Helvetica", 14))
            
            self.rock_bttn = tk.Button(self.selectionFrame, text= "Rock",
                                       width= 10, height= 5,
                                       command= self.choose_rock)
            
            self.paper_bttn = tk.Button(self.selectionFrame, text= "Paper", 
                                        width= 10, height= 5,
                                        command= self.choose_paper)
            
            self.scissors_bttn = tk.Button(self.selectionFrame, text= "Scissors", 
                                           width= 10, height= 5,
                                           command = self.choose_scissors)
            
            self.play_bttn = tk.Button(self.selectionFrame, text= "Play", width= 10,
                                       command= self.play)
            
            # Pack the contents into the frame
            self.choose_label.grid(row= 1, column= 2, padx= 10, pady= 10 )
            self.rock_bttn.grid(row= 2, column= 1, padx= 10, pady= 10)
            self.paper_bttn.grid(row= 2, column= 2, padx= 10, pady= 10)
            self.scissors_bttn.grid(row= 2, column= 3, padx= 10, pady= 10)
            self.play_bttn.grid(row= 4, column=2, padx= 10, pady= 10)
            
            '''
                End of the result frame
            '''
            
            '''
                Beginning of the score frame
            '''
            # Frame that will hold the scores of the game and also reset the labels
            self.scoreFrame = tk.Frame(self.main_window)
            self.scoreFrame.grid(row= 9, column= 2, rowspan= 7, columnspan= 7) # Pack the score frame
            
            self.score_label = tk.Label(text= "Scores: ", font= "Helvetica 16 bold")
            self.playerScore_label = tk.Label(text= "Player:")
            self.p1Score_entry = tk.Entry(self.scoreFrame, width= 5, cursor= "left_ptr")
            self.p1Score_entry.configure(state= tk.DISABLED, disabledbackground= "white", disabledforeground= "black")

            self.PCScore_label = tk.Label(text = "PC: ")
            self.pc1Score_entry = tk.Entry(self.scoreFrame, width= 5, cursor= "left_ptr")
            self.pc1Score_entry.insert(0,0)
            self.pc1Score_entry.configure(state= tk.DISABLED, disabledbackground= "white", disabledforeground= "black")

            
            
            # Pack in the frame
            self.score_label.grid(row= 8, column= 2, padx= 10, pady= 10)
            self.playerScore_label.grid(row= 9, column= 1, padx= 5, pady= 10)
            self.p1Score_entry.grid(row = 9, column= 2, padx= 5, pady= 10)
            self.PCScore_label.grid(row = 9, column= 2, padx= 5, pady= 5)
            self.pc1Score_entry.grid(row= 9, column= 3, padx= 5, pady= 5)
            
            
            
            
            # Create a menu bar at top of window
            self.menubar = tk.Menu(self.main_window)
            self.main_window.config(menu = self.menubar)
            
            # Help menu option
            self.help_menu = tk.Menu(self.menubar, tearoff = 0)
            self.menubar.add_cascade(label = "Help", menu = self.help_menu)
            self.help_menu.add_command(label = "Conditions",
                                    command = self.show_instructions)
            self.help_menu.add_command(label = "About",
                                    command = self.show_about)
            
            
            
            # Start with the window event loop
            self.main_window.mainloop()
            
    def play(self):
        pass
        
    def choose_rock(self):
        tkinter.messagebox.showinfo("Info", "You chose rock.")

    
    def choose_paper(self):
        tkinter.messagebox.showinfo("Info", "You chose paper")

    
    def choose_scissors(self):
        tkinter.messagebox.showinfo("Info", "You chose Scissors")
            
    def show_about(self):
        help_msg = "This a Rock Paper Scissors game using Tkinter\n\nWritten by: Gabriel dos Reis\n\nDate: 2023"
        tkinter.messagebox.showinfo("Help", help_msg)
        
    def show_instructions(self):
        win_conditions = "Game Winner Condition:\n\n\tPaper and Scissor => Scissor wins\n\t Rock and Scissor => Rock wins \n\t Paper and Rock => Paper wins"
        tkinter.messagebox.showinfo("Conditions", win_conditions)
        
            
            
if __name__ == "__main__":
    Game_GUI()
