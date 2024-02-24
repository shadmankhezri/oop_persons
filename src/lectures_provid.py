# from src.professor_lectures import wr
# import json


class LectuersProvide:
    def __init__(self , professor_lecture):
        self.professor_lecture = professor_lecture


    def show_provide_lecture(self):
        lectures = self.professor_lecture.lectures

        if (lectures):
            print("list of provided lectures:")
            for lecture in lectures:
                print(f"Lecture: {lecture['name']} , Unit: {lecture['unit']}")

        else:
            print("No lectures provided")


        # PATH = "./data/professors_lectures.json"
        # try:
        #     with open(PATH , 'r') as file:
        #         lectures_data = json.load(file)
        #         if (lectures_data):

        #             print("Provided Lectures")
        #             for professor , lectures in lectures_data.item():
        #                 print(f"\nProfessor: {professor}")
        #                 for lecture in lectures:
        #                     print(f"Lectures: {lecture['name']}, Unit: {lecture['unit']}")

        #         else:
        #             print("No lectures provided")
        
        # except:
        #     print("file not found.")