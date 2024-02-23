


from src.professor import Professors



class LectureLimitError(Exception):
    def __init__(self , msg = "Invalid Input. please enter a number between 1 to 5"):
        self.msg = msg
        super().__init__(self.msg)



class ProfessorLecture(Professors):
    def __init__(self, pers_id, name, family, gender, year_of_birth, prof_id, rank):
        super().__init__(pers_id, name, family, gender, year_of_birth, prof_id, rank)

        self.lectures = []



    def write_lectures(self):
        while True:
            try:
                count_lectures = int(input("Enter the number of lectures: "))
                if count_lectures < 0 or count_lectures > 5:
                    raise LectureLimitError
                break

            except ValueError:
                print("Invalid input, please do not enter str. enter int")

            except LectureLimitError as error:
                print(error)
            




        for i in range(count_lectures):
            lectures_name = input(f"Enter the name of lecture {i+1}: ")
            self.lectures.append(lectures_name)




    def show_lecture_info(self):
        print()
        self.professor_show_info()

        print("\nLectures: ")
        print(self.lectures)
