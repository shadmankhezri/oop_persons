from src.professor import Professors
from src.professor_lectures import ProfessorLecture


class ProfessorMenu:
    def __init__(self):

        self.professors = {

            "199022" : Professors("22222" , "shayan" , "khezri" , "male" , 1990 , "199022" , "B"),
            "198533" : Professors("33333" , "ahmad" , "ahmadi" , "male" , 1985 , "198533" , "D"),
            "195044" : Professors("44444" , "akram" , "akrami" , "female" , 1950 , "195044" , "A"),

        }


        self.professor_lecture = ProfessorLecture()


    def professor_menu(self):
        try:
            prof_id = input("Enter professor ID: ")
            prof = self.professors.get(prof_id)
            if (prof):
                while True:
                    print("\n---------Professor Menu---------\n")
                    print("\n1. Show Information")
                    print("2. Input Lectures")
                    print("3. Back to main menu\n")

                    try:
                        choice = int(input("Enter your choice: "))
                        if (choice == 1):
                            prof.professor_show_info()
                    
                        elif (choice == 2):
                            name = input("Enter your name: ")
                            family = input("Enter your family: ")
                            self.professor_lecture.write_lectures(name , family)
                        
                        elif (choice == 3):
                            break

                        else:
                            print("Invalid choic, please enter 1 or 2")
                    
                    except ValueError:
                        print("Invalid input, please enter a number")
                    

            else:
                raise ValueError("Incorrect professor ID")
        except ValueError:
            print(f"Invalid input")