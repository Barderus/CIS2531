import tkinter
import tkinter.messagebox
import retailItem as ri
import tkinter.font
import tkinter.filedialog


class RetailItem_GUI():
    
    # Class level variables
    COURIER_FONT = "Courier"
    TIMES_FONT = "Times New Roman"
    BOLD_FONT = 1

    def __init__(self):

        # Create a list of retailItems
        self.__retailList = []
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Retail GUI")

        # Size of the window
        self.main_window.geometry("500x500+200+200")

        # Create frame to hold retail widgets
        self.retailFrame = tkinter.Frame(self.main_window)
        self.retailFrame.grid(row=0, column=0, rowspan=3, columnspan=3)

        # Create label and entry for description
        self.desc_label = tkinter.Label(self.retailFrame, text="Description:")
        self.desc_entry = tkinter.Entry(self.retailFrame, width=20)

        # Create label and entry for inventory (units)
        self.units_label = tkinter.Label(self.retailFrame, text="Inventory:")
        self.units_entry = tkinter.Entry(self.retailFrame, width=20)

        self.price_label = tkinter.Label(self.retailFrame, text="Price:")
        self.price_entry = tkinter.Entry(self.retailFrame, width=20)

        # Place widgets in grid
        self.desc_label.grid(row=0, column=0, padx=5, pady=3)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=3)
        self.units_label.grid(row=1, column=0, padx=5, pady=3)
        self.units_entry.grid(row=1, column=1, padx=5, pady=3)
        self.price_label.grid(row=2, column=0, padx=5, pady=3)
        self.price_entry.grid(row=2, column=1, padx=5, pady=3)

        # Create frame to hold buttons
        self.buttonFrame = tkinter.Frame(self.main_window)

        # Create buttons
        self.add_button = tkinter.Button(self.buttonFrame, text="Add",
                                         command=self.add_item)
        self.show_button = tkinter.Button(self.buttonFrame, text="Display",
                                          command=self.display_items)
        self.clear_button = tkinter.Button(self.buttonFrame, text="Clear",
                                           command=self.clear_entry)
        self.exit_button = tkinter.Button(self.buttonFrame, text="Exit",
                                          command=self.exit_app)

        # Pack buttons into frame
        self.add_button.pack(side= "left", padx = 5)
        self.show_button.pack(side= "left", padx = 5)
        self.clear_button.pack(side= "left", padx = 5)
        self.exit_button.pack(side= "left", padx = 5)
        
        # Create a frame to hold font selection widgets and listbox
        self.displayFrame = tkinter.Frame(self.main_window)
        
        # Check button for font weight
        self.font_weight = tkinter.IntVar()
        self.font_weight.set(RetailItem_GUI.BOLD_FONT)
        self.bold_check = tkinter.Checkbutton(self.buttonFrame, text = "Bold",
                                              variable = self.font_weight)
        
        # Rdio button for font family
        self.font_fam = tkinter.StringVar()
        self.font_fam.set(RetailItem_GUI.COURIER_FONT)
        self.courier_button = tkinter.Radiobutton(self.displayFrame, 
                                                  text = "Courier",
                                                  variable = self.font_fam,
                                                  value = RetailItem_GUI.COURIER_FONT)
        
        self.times_button = tkinter.Radiobutton(self.displayFrame, 
                                                text = "Times",
                                                variable = self.font_fam,
                                                value = RetailItem_GUI.BOLD_FONT)
        
        # Scrollbar and listbox
        self.scrollbar = tkinter.Scrollbar(self.displayFrame, orient = tkinter.VERTICAL)
        self.listbox = tkinter.Listbox(self.displayFrame,
                                        yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.listbox.yview)
        
        # Pack radio buttons, scroll bar, and listbox
        self.courier_button.pack(side = "left")
        self.times_button.pack(side = "left")
        self.bold_check.pack(side = "left")
        self.scrollbar.pack(side = "right", fill = tkinter.Y)
        self.listbox.pack(side = "left", fill = tkinter.BOTH, expand = 1)

        # Place frames into window
        self.retailFrame.pack(side = "top", pady = 5)
        self.buttonFrame.pack(side = "top", pady = 5)
        self.displayFrame.pack(side = "top", pady = 5)
        
        # Create a menu bar at top of windw
        self.menubar = tkinter.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        # aAdd file menu options
        self.file_menu = tkinter.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label = "Save Inventory...", command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.exit_app)
        
        # Start with the window event loop
        self.main_window.mainloop()

    def add_item(self):
        # Get text from entry fields
        desc = self.desc_entry.get()
        unit = self.units_entry.get()
        price = self.price_entry.get()

        # Check for positive integer for inventory amount
        try:
            unit = int(unit)
            if unit < 0:
                raise ValueError()
        except ValueError:
            # Display error message box
            tkinter.messagebox.showerror("ERROR",
                                         "Invetory must be positive integer number.")

            # Set focus to inventory
            self.units_entry.focus()

        else:
            # Check for positive price amount
            try:
                price = float(price)
                if price < 0:
                    raise ValueError()
            except ValueError:
                # Display error message box
                tkinter.messagebox.showerror("ERROR",
                                             "Price must be positive amount.")

                # Set focus to price
                self.price_entry.focus()
            else:
                # Create and add retail item to the list
                self.__retailList.append(ri.RetailItem(desc,
                                                       int(unit),
                                                       float(price)))
                # Display confirmation message box
                tkinter.messagebox.showinfo("Information",
                                            "Item added to the inventory")
                # Reset fields
                self.clear_entry()

    def display_items(self):
        # Clear list box
        self.listbox.delete(0, tkinter.END)
        # Check user selection for font type and set listbox font
        if self.font_weight.get() == RetailItem_GUI.BOLD_FONT:
            fontUse = tkinter.font.Font(family = self.font_fam.get(),
                                     weight = "bold")
        else:
            fontUse = tkinter.font.Font(family = self.font_fam.get(),
                                     weight = "normal")
        
        self.listbox.config(font = fontUse)
            
        # Add retail items to listbox
        for item in self.__retailList:
            item_string = "{:5} {:3} {:.2f}".format(item.description,
                                                    item.units,
                                                    item.price)
            self.listbox.insert(tkinter.END, item_string)

    def clear_entry(self):
        # Remove all text from entry fields
        self.desc_entry.delete(0, tkinter.END)
        self.units_entry.delete(0, tkinter.END)
        self.price_entry.delete(0, tkinter.END)

        # Set the focus to description
        self.desc_entry.focus()

    def exit_app(self):
        response = tkinter.messagebox.askyesno("Confirmation",
                                               "Are you sure you want to exit?")
        if response == True:
            self.main_window.destroy()
            
        # Menu option functions
    def save_file(self):
        # Get filename
        file_name = tkinter.filedialog.asksaveasfilename(initialdir = "/",
                                                    filetypes = [("Text files", "*.txt"),
                                                                 ("All files",".*")],
                                                    title = "Select file",
                                                    defaultextension = ".txt") 
        # Check for empty string
        if len(file_name) != 0:
            # Open file
            self.file_var = open(file_name, "w")
            
            # Write to file
            for item in self.__retailList:
                item_string = "{}:{}:{}".format(item.description,
                                                        item.units,
                                                        item.price)
                self.file_var.write(item_string + "\n")
            
            # Close file
            self.file_var.close()


if __name__ == "__main__":
    RetailItem_GUI()
