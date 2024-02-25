

class StudentSelectLectures:
    def __init__(self):
        self.select_lectures_list = []


    def save_selection(self , name):

        PATH = f"./data/{name}_lectures.txt"
        
        with open(PATH , "w") as file:
            for lecture in self.select_lectures_list:
                file.write(f"{lecture[0]} - unit:{lecture[1]}\n")

        print("Lectures selection saved")




    def load_selection(self , name):
        PATH = f"./data/{name}_lectures.txt"

        try:
            with open(PATH , 'r') as file:
                lines = file.readlines()
                print(f"\nLectures Selection for {name}\n")
                for line in lines:
                    print(line.strip())

        except:
            print("No lectures selection found")




    def select_unit(self , name):

        count_lecture = int(input("Enter the number of lectures you want to select: "))

        for i in range(count_lecture):
            lecture_name = input(f"Enter the name of lecture {i+1}: ")
            lecture_unit = int(input(f"Enter the unit of lecture {lecture_name}: "))
            self.select_lectures_list.append((lecture_name , lecture_unit))

        print("\nUnit selection was done successfully")
        self.save_selection(name)

