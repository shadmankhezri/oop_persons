"""
In this module, we have created class StudentMenu and imported class Student to create a dictionary of objects 
in the init function.
If the user enters as a student, he/she will input the ID in the first step and then the name of the student. 
If an ID is in the objects dictionary, it shows the menu related to the student
In the menu, the student has 4 choices that he/she can see all his/her information based on the ID entered. 
or to see the lectures given by the professors. And can also enter the unit selection section to take the lectures

"""

# Import of required classes

from src.student import Students
from src.lectures_provid import LectuersProvide
from src.professor_lectures import ProfessorLecture
from src.select_lectures import StudentSelectLectures



class StudentMenu:
    def __init__(self):

        self.students = {              # make students object from class Students with dict

            "199511" : Students("11111" , "shadman" , "khezri" , "male" , "1995" , 2022 , "199511"),
            "200022" : Students("22222" , "test" , "testi" , "male" , 2000 , 2023 , "200022"),

        }

        # create an objects from this classes for show lectures and select lectures
        
        self.professor_lecture = ProfessorLecture()
        self.lectuers_provid = LectuersProvide()
        self.student_select_lectures = StudentSelectLectures()
        # self.lectuers_provid = LectuersProvide(self.professor_lecture)


    def student_menu(self):
        try:

            std_id = input("Enter student ID: ")       # in the first step get the ID and
            std = self.students.get(std_id)            # if it is in the class objects,
                                                       # it returns True and displays the professor's menu
            
            name = input("Enter your name: ")          # get name for save select lectures
                                                       # special for each students
        
            if (std):                                   
            
                while True:
                    print("\n---------Student Menu---------\n")
                    print("\n1. Show Information")
                    print("2. Lectures provided")
                    print("3. select Unit")
                    print("4. Show Unit")
                    print("5. Back to main menu\n")

                    try:
                        choice = int(input("Enter your choice: "))
                        if (choice == 1):
                            std.student_show_info()         # call this def from student module based on ID


                        elif (choice == 2):                 # call this def from lectures_provid modul
                                                            # and show the information about lectures
                            self.lectuers_provid.show_provide_lecture()


                        elif (choice == 3):                 # call this def from select_lectures module
                                                            # and send name for save txt file special each student
                            self.student_select_lectures.select_unit(name) 


                        elif (choice == 4):                 # call this def from select_lectures module
                                                            # show the list of lectures selected by each student
                            self.student_select_lectures.load_selection(name)


                        elif (choice == 5):
                            break

                        else:                                             # if student input wrong number 
                            print("Invalid choic, please enter 1 to 5")
                            
                    except ValueError:                                    # if student input string 
                        print("Invalid input, please enter a number")


            else:                       # if the student input wrong ID
                raise ValueError
        except ValueError:
            print("Incorrect student ID")