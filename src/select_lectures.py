"""
In this class, which we have built the related object in student_menu module , we have done the tasks 
related to show the lectures and selecting and saving the lectures.

We have created an empty list inside the init function because we need it to save and select lectures.

In def save_selection(), we save the lectures that the student has select in a txt file for that student.

Inside def load_selection(), when the student wants to see the list of lectures he has select, 
he will see the content of the txt file related to him, and if he has not select a course and has 
no txt file, the program will not stop because we have managed it with try and except.

And then in def select_unit(), when the student wants to select a lectures,you must first enter 
the number of lectures that wants. Then, based on that number, must enter the name of the lectures
and its unit, and every time these are stored in the empty list that we created above, 
and then calls def save_selection() to save the selected lecturess in txt file.
"""

class StudentSelectLectures:
    def __init__(self):
        self.select_lectures_list = []

    # for save lectures in txt file
    def save_selection(self , name):

        PATH = f"./data/{name}_lectures.txt"
        
        with open(PATH , "w") as file:
            for lecture in self.select_lectures_list:
                file.write(f"{lecture[0]} - unit:{lecture[1]}\n")

        print("Lectures selection saved")



    # for show select and unit of lectures
    def load_selection(self , name):
        PATH = f"./data/{name}_lectures.txt"

        try:
            with open(PATH , 'r') as file:
                lines = file.readlines()
                print(f"\nLectures Selection for {name}\n")
                for line in lines:
                    print(line.strip())

        except:                    # if not exist txt file, 
            print("No lectures selection found")



    # for select unit by student
    def select_unit(self , name):

        count_lecture = int(input("Enter the number of lectures you want to select: "))

        for i in range(count_lecture):

            lecture_name = input(f"Enter the name of lecture {i+1}: ")
            lecture_unit = int(input(f"Enter the unit of lecture {lecture_name}: "))

            # save the input lectures in the list
            self.select_lectures_list.append((lecture_name , lecture_unit)) 

        print("\nUnit selection was done successfully")

        # then call this for save data in list to txt file
        self.save_selection(name)

