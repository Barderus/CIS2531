'''
Author: Gabriel dos Reis
Date: 12/4/2023
Description: This program creates a GUI to schedule students and courses.
    
'''
import tkinter as tk
import student as stu
import course as crs
import tkinter.messagebox
import tkinter.filedialog
import tkinter.font

class ScheduleGUI:
    ''' This class creates a GUI to schedule students and courses.'''
    
    # Class level variables
    COURIER_FONT = "Courier"
    TIMES_FONT = "Times New Roman"
    BOLD_FONT = 1
    SIZE12_FONT = 12
    SIZE14_FONT = 14
    SIZE16_FONT = 16
    
    def __init__(self):
        
        ''' Initialize the GUI '''
       
        # Create a list of students and courses
        self.__student_list = []
        self.__course_list = []
        
        # Set the selected student id to None
        self.__selected_student_id = None

         
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Scheduler GUI")
        
        # Size of the window
        self.main_window.geometry("750x400+250+150")
        
        # Create frame to hold student widgets
        self.studentFrame = tk.Frame(self.main_window)
        self.studentFrame.grid(row=0, column=0, rowspan=3, columnspan=3)

        # Create some labels and entry for placement
        # Student name
        self.lblName = tk.Label(self.studentFrame, text= "Student Name: ")
        self.entryName = tk.Entry(self.studentFrame, width= 20)
        # Student ID
        self.lblID = tk.Label(self.studentFrame, text= "Student ID: ")
        self.entryID = tk.Entry(self.studentFrame, width= 20)
        # Student GPA
        self.lblGPA = tk.Label(self.studentFrame, text= "GPA: ")
        self.entryGPA = tk.Entry(self.studentFrame, width= 20)
        
        # Place widgets using grid on the student frame
        self.lblName.grid(row=0, column=0, padx=5, pady=3)
        self.entryName.grid(row=0, column=1, padx=5, pady=3)
        
        self.lblID.grid(row=1, column=0, padx=5, pady=3)
        self.entryID.grid(row=1, column=1, padx=5, pady=3)
        
        self.lblGPA.grid(row=2, column=0, padx=5, pady=3)
        self.entryGPA.grid(row=2, column=1, padx=5, pady=3)
        
        # Create frame to hold course widgets
        self.courseFrame = tk.Frame(self.main_window)
        self.courseFrame.grid(row=3, column=6, rowspan=3, columnspan=6,padx=50)

        # Crate some labels and entry for placement
        # Course ID
        self.lblCourseID = tk.Label(self.courseFrame, text= "Course ID: ")
        self.entryCourseID = tk.Entry(self.courseFrame, width= 20)
        # Course name
        self.courseName = tk.Label(self.courseFrame, text= "Course Name: ")
        self.entryCourseName = tk.Entry(self.courseFrame, width= 20)
        # Credit hours
        self.crHours = tk.Label(self.courseFrame, text= "Credit Hours: ")
        self.entryCrHours = tk.Entry(self.courseFrame, width= 20)
        
        # Places widgets using grid on the course frame
        self.lblCourseID.grid(row=0, column=6, padx=5, pady=3)
        self.entryCourseID.grid(row=0, column=7, padx=5, pady=3)
        
        self.courseName.grid(row=1, column=6, padx=5, pady=3)
        self.entryCourseName.grid(row=1, column=7, padx=5, pady=3)
        
        self.crHours.grid(row=2, column=6, padx=5, pady=3)
        self.entryCrHours.grid(row=2, column=7, padx=5, pady=3)
        
        # Create frames to hold buttons
        self.buttonStuFrame = tk.Frame(self.main_window)
        self.buttonCrsFrame = tk.Frame(self.main_window)

        # Create buttons
        # For the student frame
        self.addStu_button = tk.Button(self.buttonStuFrame, text="Add Student",
                                         command=self.add_student)
        self.showStu_button = tk.Button(self.buttonStuFrame, text="Display Students",
                                          command=self.display_students)
        # For the course frame
        self.addCourse_button = tk.Button(self.buttonCrsFrame, text="Add Course",
                                           command=self.add_course)        
        
        # Pack buttons in the frame
        self.addStu_button.pack(side= "left", padx = 5)
        self.showStu_button.pack(side= "left", padx = 5)
        self.addCourse_button.pack(side= "left", padx = 5)
        
        # Place the frames using grid
        self.buttonStuFrame.grid(row=5, column=0, columnspan=3, pady=5)
        self.buttonCrsFrame.grid(row=5, column=3, columnspan=6, pady=5)

        
        # Create a frame to hold list boxes and scrollbars
        self.displayStu_Frame = tkinter.Frame(self.main_window)   
             
        # Scrollbar and listbox to hold the student data
        self.stuscrollbar = tkinter.Scrollbar(self.displayStu_Frame, orient = tkinter.VERTICAL)
        self.stulistbox = tkinter.Listbox(self.displayStu_Frame,
                                        yscrollcommand = self.stuscrollbar.set, width= 50)
        self.stuscrollbar.config(command = self.stulistbox.yview)
        
        self.stuscrollbar.pack(side = "right", fill = tkinter.Y)
        self.stulistbox.pack(side = "left", fill = tkinter.BOTH, expand = 1)
        
        # Create frame to hold buttons and radio buttons
        self.control_frame = tk.Frame(self.main_window) 
        
        # Radio button for font family
        self.font_fam = tk.StringVar()
        self.font_fam.set(ScheduleGUI.COURIER_FONT)
        self.create_button = tk.Button(self.control_frame, text="Create schedule", width=15,
                                         command=self.create_schedule)
        self.font_label = tk.Label(self.control_frame, text = "Font Family")
        self.courier_button = tk.Radiobutton(self.control_frame, 
                                                  text = "Courier",
                                                  variable = self.font_fam,
                                                  value = ScheduleGUI.COURIER_FONT)
        
        self.times_button = tk.Radiobutton(self.control_frame, 
                                                text = "Times",
                                                variable = self.font_fam,
                                                value = ScheduleGUI.BOLD_FONT)
    
        # Radio button for font size
        self.font_size = tk.IntVar()
        self.font_size.set(self.SIZE12_FONT)
        self.data_check = tk.IntVar()
        self.data_check.set(0)
        
        self.size_label = tk.Label(self.control_frame, text = "Font Size")
        self.size12_button = tk.Radiobutton(self.control_frame,
                                                 text="12",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE12_FONT)
        self.size14_button = tk.Radiobutton(self.control_frame,
                                                 text="14",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE14_FONT)
        self.size16_button = tk.Radiobutton(self.control_frame,
                                                 text="16",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE16_FONT)

        # Check button for font weight
        self.font_weight = tkinter.IntVar()
        self.font_weight.set(ScheduleGUI.BOLD_FONT)   
        self.bold_check = tkinter.Checkbutton(self.control_frame, text = "Bold",
                                              variable = self.font_weight)              

        
        # Grid layout for the widgets in the control frame
        self.create_button.grid(row=1, column=4, pady=5, padx=5, sticky="w")
        self.font_label.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        self.size_label.grid(row=0, column=2, pady=5, padx=10, sticky="w")

        self.courier_button.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.times_button.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.size12_button.grid(row=1, column=2, pady=5, padx=10, sticky="w")
        self.size14_button.grid(row=2, column=2, pady=5, padx=10, sticky="w")
        self.size16_button.grid(row=3, column=2, pady=5, padx=10, sticky="w")
        
        self.bold_check.grid(row=0, column=4, pady=5, padx=10, sticky="w")
        
        self.save_button = tk.Button(self.control_frame, text="Save to file", command=self.save_file)
        self.save_button.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        
        self.load_button = tk.Button(self.control_frame, text="Load from file", command=self.load_data)
        self.load_button.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        # Place frames into the window
        self.studentFrame.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.courseFrame.grid(row=0, column=3, rowspan=3, columnspan=6)
        self.displayStu_Frame.grid(row=7, column=0, rowspan=3, columnspan=3, padx=10)
        self.control_frame.grid(row=9, column=3, rowspan=3, columnspan=3, padx = 20)
        
        # Create a menu bar at top of windw
        self.menubar = tkinter.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        # Add file menu options
        self.file_menu = tkinter.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label = "Save file...", command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.exit_app)
        
        # Help menu option
        self.help_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Help", menu = self.help_menu)
        self.help_menu.add_command(label = "About",
                                   command = self.show_about)
       
        # Start with the window event loop
        self.main_window.mainloop()
        
    def add_student(self):
        
        ''' This method adds a student to the list '''
        
        # Get text from entry fields
        stu_id = self.entryID.get()
        stu_name = self.entryName.get()
        stu_gpa = self.entryGPA.get()

        # Check for empty string
        if not stu_id or not stu_name or not stu_gpa:
            # Display error message box
            tkinter.messagebox.showerror("ERROR", "All fields must be filled.")
            self.entryID.focus()
            return

        try:
            # Try to convert gpa to a float
            stu_gpa = float(stu_gpa)
        except ValueError:
            # Display an error if the conversion fails
            tkinter.messagebox.showerror("ERROR", "Student GPA must be a float.")
            self.entryGPA.focus()
            return

        # Check if the student ID already exists
        for student_obj in self.__student_list:
            if student_obj.id_num == stu_id:
                # Display an error if the ID is already in use
                tkinter.messagebox.showerror("ERROR", "Student ID already exists.")
                self.entryID.focus()
                return

        # Create a student object and add it to the list
        new_student = stu.Student(name=stu_name, id_num=stu_id, gpa=stu_gpa)
        self.__student_list.append(new_student)

        # Display confirmation message box
        tkinter.messagebox.showinfo("Information", "Student added to the list")

        # Clear the entry fields
        self.clear_stuentry()
  
    def add_student_from_file(self, stu_id, stu_name, stu_gpa, course_list):
        ''' This method adds a student to the list from a file '''
        
        # Validate data
        if not stu_id:
            print("Invalid data in file: Student ID is missing.")
            return

        if not stu_name:
            print("Invalid data in file: Student name is missing.")
            return

        if not stu_gpa:
            print("Invalid data in file: GPA is missing.")
            return

        try:
            stu_gpa = float(stu_gpa)
        except ValueError:
            print("Invalid data in file: GPA must be a float.")
            return

        # Create a student object and add it to the list
        new_student = stu.Student(name=stu_name, id_num=stu_id, gpa=stu_gpa)

        for course_info in course_list:
            new_student.addCourse(course_info)

        self.__student_list.append(new_student)
        self.display_students()

        

    def add_course(self):
        ''' This method adds a course to the selected student'''
        # Check if a student is selected
        if self.__selected_student_id is None:
            tkinter.messagebox.showerror("Error", "Please select a student first.")
            return

        # Get text from entry fields
        crs_ID = self.entryCourseID.get()
        crs_name = self.entryCourseName.get()
        crs_crdHours = self.entryCrHours.get()

        # Check for empty string
        if not crs_ID or not crs_name or not crs_crdHours:
            tkinter.messagebox.showerror("ERROR", "All fields must be filled.")
            return

        try:
            # Try to convert credit hours to an integer
            crs_crdHours = int(crs_crdHours)
        except ValueError:
            tkinter.messagebox.showerror("ERROR", "Credit hours must be an integer.")
            self.entryCrHours.focus()
            return

        # Create a Course object
        new_course = crs.Course(num=crs_ID, name=crs_name, crHours=crs_crdHours)

        # Find the selected student in the list
        selected_student = None
        for student_obj in self.__student_list:
            if student_obj.id_num == self.__selected_student_id:
                selected_student = student_obj
                break

        if selected_student:
            # Add the course to the selected student's list of courses
            selected_student.courses.add(new_course)
            tkinter.messagebox.showinfo("Information", "Course added to the selected student.")
        
        ''' Testing purposes
        for courses in selected_student.courses:
            print("Courses: ", courses)
        '''

        # Clear the entry fields
        self.clear_crsentry()
        '''
        # PRINT FOR TESTING
        print(f"Selected Student ID: {self.__selected_student_id}")
        print(f"Selected Student Data: {selected_student}")
        '''

    def display_students(self):
        ''' This method displays the students in the listbox '''
        
        # Clear the listbox before adding new items
        self.stulistbox.delete(0, tkinter.END)

        # Add students items to listbox
        for student_obj in self.__student_list:
            # Check if the item is an instance of Student class
            if isinstance(student_obj, stu.Student):
                # Extract necessary information from the student object
                item_string = f"Name:{student_obj.name} ID:{student_obj.id_num} GPA:{student_obj.gpa}"
                # Add the item to the listbox
                self.stulistbox.insert(tkinter.END, item_string)

        # Bind the select_student method to the listbox
        '''
            The .bind method allows us to bind a function to an event, in this case, the event is when an item is selected in the listbox.
        '''
        self.stulistbox.bind('<<ListboxSelect>>', self.select_student)

    def select_student(self, event):
        # Get the index of the selected item in the listbox
        index = self.stulistbox.curselection()
        
        # If an item is actually selected, it gets the student object ID from the list
        if index:
            selected_student = self.__student_list[index[0]]
            # Update the selected student ID for reference
            self.__selected_student_id = selected_student.id_num
            
    def load_data(self):
        ''' This method loads data from a file'''
        
        # Clear the listbox before adding new data
        self.stulistbox.delete(0, tk.END)
        
        # Get filename
        file_path = tkinter.filedialog.askopenfilename(initialdir="/",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", ".*")],
                                                   title="Select file")
        # Check if the user selected a file
        if file_path:
            # Read data from the file
            with open(file_path, "r") as file:
                    for line in file:
                        # Split the line into fields using comma as a delimiter
                        stu_id, stu_name, stu_gpa, *self.__course_list = line.strip().split(",")
                        ''' Testing purposes
                        print(F"ID: {stu_id}, Name: {stu_name}, GPA: {stu_gpa}, Courses: {self.__course_list}")
                        '''
                        # Call the add_student_from_file method to add the student to the list
                        self.add_student_from_file(stu_id, stu_name, stu_gpa, self.__course_list)
                               
    def create_schedule(self):
        '''This method creates a schedule for the selected student in the listbox and save it as studentSchedule.txt'''

        # Check if a student is selected
        if self.__selected_student_id is None:
            tkinter.messagebox.showerror("Error", "Please select a student first.")
            return

        # Use a specific filename
        file_name = "studentSchedule.txt"

        # Open file
        with open(file_name, "w") as file_var:
            # Find the selected student in the list
            # Loop through each student_obj in the list of students
            for student_obj in self.__student_list:
                # Check if the id_num of the current student_obj matches the selected student id
                if student_obj.id_num == self.__selected_student_id:
                    # If there's a match, assign the current student_obj to selected_student
                    selected_student = student_obj

            if selected_student:
                # Set the font configuration for writing to the file
                font_weight = "normal"
                if self.font_weight.get() == ScheduleGUI.BOLD_FONT:
                    font_weight = "bold"
                font_family = self.font_fam.get()
                font_use = tkinter.font.Font(family=font_family, weight=font_weight)

                # Write student information to file
                file_var.write("ID: {} Name: {} GPA: {}\n".format(selected_student.id_num, selected_student.name, selected_student.gpa))
                file_var.write("\nCourses:\n")
                
                # Write each course for the student
                for course in selected_student.courses:
                    file_var.write("    {}\n".format(course))

        tkinter.messagebox.showinfo("Information", "Schedule written to the file studentSchedule.txt.")



    def clear_stuentry(self):
        ''' This method clears the entry fields'''
        # Remove all text from entry fields
        self.entryID.delete(0, tkinter.END)
        self.entryName.delete(0, tkinter.END)
        self.entryGPA.delete(0, tkinter.END)

        # Set the focus to description
        self.entryID.focus()

    def clear_crsentry(self):
        ''' This method clears the entry fields for courses'''
        # Remove all text from entry fields
        self.entryCourseID.delete(0, tkinter.END)
        self.entryCourseName.delete(0, tkinter.END)
        self.entryCrHours.delete(0, tkinter.END)

        # Set the focus to description
        self.entryCourseID.focus()
    
    def save_file(self):
        ''' This method saves the data to a file'''
        # Get filename
        file_name = tkinter.filedialog.asksaveasfilename(initialdir="/",
                                                        filetypes=[("Text files", "*.txt"),
                                                                    ("All files", ".*")],
                                                        title="Select file",
                                                        defaultextension=".txt")
        # Check for empty string
        if len(file_name) != 0:
            # Open file
            with open(file_name, "w") as file_var:
                # Write to file
                for student_obj in self.__student_list:
                    # Extract necessary information from the student object using the methods join and map
                    '''
                        .join method joins the elements of an iterable to the end of the string using comma as the delimeter field
                        map fuction returns a list of the results after applying the str() function to each course in the list of courses
                            https://realpython.com/python-map-function/#transforming-iterables-of-strings-with-pythons-map
                        
                    '''
                    item_string = f"{student_obj.id_num},{student_obj.name},{student_obj.gpa},{','.join(map(str, student_obj.courses))}"

                    file_var.write(item_string + "\n")

            tkinter.messagebox.showinfo("Information", "File saved successfully.")

    def show_about(self):
        ''' This method displays information about the program and the author '''
        tk.messagebox.showinfo("Help", "This is a GUI application designed to create schedule of students.\n\nWritten by: Gabriel dos Reis\n\nDate: 2023")
        
    def exit_app(self):
        ''' This method allows the user to exit the program'''
        response = tkinter.messagebox.askyesno("Confirmation",
                                               "Are you sure you want to exit?")
        if response == True:
            self.main_window.destroy()
    
if __name__ == '__main__':
    ''' Launch the application '''
    launch = ScheduleGUI()