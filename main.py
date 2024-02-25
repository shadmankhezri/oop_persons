"""
In this file, we created the Menu class and also imported two classes StudentMenu and ProfessorMenu
from src. Then, inside the init of the Menu class, we have created an object from two classes StudentMenu
and ProfessorMenu. Then inside the main_menu() function. We will create the main menu that will ask the user 
whether to enter as professor or as student. And also, we have managed the possibility of input error with
try and except so that if the user enters a wrong number, the program does not stop and request again.
"""

# example for student ----->  {name : shadman , family : khezri , id : 199511}
# example for student ----->  {name : test , family : testi, id : 200022}

# example for professor ----->  {name : shayan , family : khezri , id : 199022}
# example for professor ----->  {name : akram , family : akrami , id : 195044}
# example for professor ----->  {name : ahmadi , family : ahmad , id : 198533}




# Import of required classes

from src.student_menu import StudentMenu
from src.professor_menu import ProfessorMenu

class Menu:
    def __init__(self):
        
        self.object_student_menu = StudentMenu()          # make object from StudentMenu class for call functions
        self.object_professor_menu = ProfessorMenu()      # make object from ProfessorMenu class for call functions


    def main_menu(self):

        while True:
            print("\n---------Menu---------\n")
            print("1. professor")
            print("2. Student")
            print("3. Exit\n")

            try:
                choice = int(input("Enter your choice: "))

                if (choice == 1):                                 
                    self.object_professor_menu.professor_menu()    # call def professor_menu by created object
                
                elif (choice == 2):
                    self.object_student_menu.student_menu()        # call def student_menu by created object

                elif (choice == 3):
                    print("Exit the program")
                    break

                else:                          # If the input number is not 1, 2, or 3, this line will be executed
                    raise ValueError                         
            
            except ValueError:                # If the user enters a string, this line will be executed
                print("Invalid input, please enter a number")

if __name__ == "__main__":
    menu = Menu()                       # make object from Menu class
    menu.main_menu()                    # call main_menu() by created object