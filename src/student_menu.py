
from src.student import Students
from src.lectures_provid import LectuersProvide
from src.professor_lectures import ProfessorLecture
from src.select_lectures import StudentSelectLectures



class StudentMenu:
    def __init__(self):

        self.students = {

            "199511" : Students("11111" , "shadman" , "khezri" , "male" , "1995" , 2022 , "199511"),
            "200022" : Students("22222" , "test" , "testi" , "male" , 2000 , 2023 , "200022"),

        }

        self.professor_lecture = ProfessorLecture()
        self.lectuers_provid = LectuersProvide(self.professor_lecture)
        self.student_select_lectures = StudentSelectLectures()

    def student_menu(self):
        try:
            std_id = input("Enter student ID: ")
            std = self.students.get(std_id)

            name = input("Enter your name: ")
            # name = self.students.get(name)
        
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
                            std.student_show_info()



                        elif (choice == 2):
                            self.lectuers_provid.show_provide_lecture()



                        elif (choice == 3):
                            self.student_select_lectures.select_unit(name)


                        elif (choice == 4):

                            self.student_select_lectures.load_selection(name)


                        elif (choice == 5):
                            break

                        else:
                            print("Invalid choic")
                            
                    except ValueError:
                        print("Invalid input, please enter a number")



            else:
                raise ValueError("Incorrect student ID")
        except ValueError as error:
            print(f"Error: {error}")