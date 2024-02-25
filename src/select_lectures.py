import json

class StudentSelectLectures:
    def __init__(self):
        self.select_lectures_list = []


    def save_selection(self):
        with open("selected_lectures.json" , "w") as file:
            json.dump(self.select_lectures_list , file)



    def load_selection(self):
        with open("selected_lectures.json" , "r") as file:
            self.select_lectures_list = json.load(file)



    def select_unit(self):

        count_lecture = int(input("Enter the number of lectures you want to select: "))
        for i in range(count_lecture):
            lecture_name = input(f"Enter the name of lecture {i+1}: ")
            lecture_unit = int(input(f"Enter the unit of lecture {lecture_name}: "))
            self.select_lectures_list.append((lecture_name , lecture_unit))
        print("\nUnit selection was done successfully")
        self.save_selection()

        
    def get_lectures_list(self):
        return self.select_lectures_list