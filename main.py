
from src.student import Students
from src.professor import Professors
from src.professor_lectures import ProfessorLecture



student_1 = Students("11111" , "shadman" , "khezri" , "male" , "1995" , 2022 , "202211")
professor_1 = ProfessorLecture("22222" , "shayan" , "khezri" , "male" , 1990 , "199022" , "A")





print("\n----------Students Info----------\n")
print("Student 1:")
student_1.student_show_info()



print("\n----------Professors Info----------\n")
print("Professor 1:")
professor_1.write_lectures()
professor_1.show_lecture_info()