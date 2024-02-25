import json


class LectuersProvide:
    def __init__(self , professor_lecture):
        self.professor_lecture = professor_lecture





    def read_json(self):

        lecture_data = []
        PATH = "./data/professors_lectures.json"
    
        with open(PATH , 'r') as file:
            lecture_data = json.load(file)
        
        return lecture_data




    def show_provide_lecture(self):
        lecture_data = self.read_json()

        if (lecture_data):
            print("provided lectures:")

            for professor_data in lecture_data:

                for professor , lectures in professor_data.items():
                    print(f"\nProfessor: {professor}")

                    for lecture in lectures:
                        print(f"Lectures: {lecture['name']}, Unit: {lecture['unit']}")
                    

        else:
            print("No lectures provided")
