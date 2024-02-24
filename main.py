
    
from src.student import Students
from src.professor import Professors
from src.professor_lectures import ProfessorLecture


class Menu:
    def __init__(self):
        self.students = {
            "199511" : Students("11111" , "shadman" , "khezri" , "male" , "1995" , 2022 , "199511"),
            "200022" : Students("22222" , "test" , "testi" , "male" , 2000 , 2023 , "200022"),
        }


        self.professors = {
            "199022" : Professors("22222" , "shayan" , "khezri" , "male" , 1990 , "199022" , "B"),
            "198533" : Professors("33333" , "ahmad" , "ahmadi" , "male" , 1985 , "198533" , "D"),
            "195044" : Professors("44444" , "akram" , "akrami" , "female" , 1950 , "195044" , "A"),
        }

        self.professor_lecture = ProfessorLecture()


    

    def student_info(self):
        try:
            std_id = input("Enter student ID: ")
            std = self.students.get(std_id)
            
            if (std):
                std.student_show_info()

            else:
                raise ValueError("Incorrect student ID")
        except ValueError as error:
            print(f"Error: {error}")


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
        except ValueError as erro:
            print(f"Error: {erro}")


    
    def main_menu(self):
        while True:
            print("\n---------Menu---------\n")
            print("1. professor")
            print("2. Student")
            print("3. Exit\n")


            try:
                choice = int(input("Enter your choice: "))

                if (choice == 1):
                    self.professor_menu()
                
                
                elif (choice == 2):
                    self.student_info()

                elif (choice == 3):
                    print("Exit the program")
                    break

                else:
                    raise ValueError("Invalid choice. please enter 1,2 or 3")
            
            except ValueError as error:
                print("Error: {error}")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()