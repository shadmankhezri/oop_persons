"""
In this module, we have created class ProfessorMenu and made an object from class Professors in the init function,
and we have also created an object from class ProfessorMenu itself, and then we have written a professor_menu()
function to create a menu for professors. If the user is entered 1 as a professor in the main menu. 
This function should be executed and its special menu for proffesor will be seen.
Also, we have imported class Professors from module professor to create an object from this class.
In the professor's menu, when you enter, you can see your personal information or input lectures to teach
"""

# Import of required classes

from src.professor import Professors
from src.professor_lectures import ProfessorLecture

class ProfessorMenu:
    def __init__(self):

        self.professors = {           # make professors object from class Professors with dict

            "199022" : Professors("22222" , "shayan" , "khezri" , "male" , 1990 , "199022" , "B"),
            "195044" : Professors("44444" , "akram" , "akrami" , "female" , 1950 , "195044" , "A"),
            "198533" : Professors("33333" , "ahmad" , "ahmadi" , "male" , 1985 , "198533" , "D"),

        }

        # make object from class ProfessorLecture for call def write_lectures()
        self.professor_lecture = ProfessorLecture()      


    def professor_menu(self):            # creat this def for make professor_menu
        try:
    
            prof_id = input("Enter professor ID: ")   # in the first step get the ID and
            prof = self.professors.get(prof_id)       # if it is in the class objects,
                                                      # it returns True and displays the professor's menu
            if (prof):                                
                while True:
                    print("\n---------Professor Menu---------\n")
                    print("\n1. Show Information")
                    print("2. Input Lectures")
                    print("3. Back to main menu\n")

                    try:
                        choice = int(input("Enter your choice: "))
                        if (choice == 1):
                                         # The display function is called with the special ID entered by the user
                            prof.professor_show_info()         # and the information related to the ID is displayed
                                                                              
                                                            
                        elif (choice == 2):
                            name = input("Enter your name: ")     # First, we get the name and surname from the user
                            family = input("Enter your family: ")

                            # then using the object we created from class ProfessorLecture
                            # we call the write_lectures() to input lectures.
                            self.professor_lecture.write_lectures(name , family)
                        
                        elif (choice == 3):
                            break

                        else:                              # If the professor enters a number other than 1, 2 and 3
                            print("Invalid choic, please enter 1 or 2")
                    
                    except ValueError:                     # if the professor input string
                        print("Invalid input, please enter a number")
                    

            else:
                raise ValueError          # if the professor input wrong ID with number
            
        except ValueError:                # if the professor input wrong ID with string
            print(f"Invalid input")