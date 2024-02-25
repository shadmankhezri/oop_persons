"""
In this module, we have Class LectuersProvide, which we have created an object for in student_menu modul, 
and when the student wants to see the list of lectures provided by the professors, the functions here are used.
When def show_provide_lecture() is called, first def read_json() is executed and the information 
inside Json is returned. And then we use this information in def show_provide_lecture().


"""

import json

class LectuersProvide:
    # def __init__(self , professor_lecture):
    #     self.professor_lecture = professor_lecture



    def read_json(self):

        lecture_data = []
        PATH = "./data/professors_lectures.json"
    
        with open(PATH , 'r') as file:
            lecture_data = json.load(file)
        
        return lecture_data      # return the information in json




    def show_provide_lecture(self):
        lecture_data = self.read_json()

        if (lecture_data):                 
            print("\nprovided lectures:")

            # lecture_data is json format and its like dict
            for provid_lectures in lecture_data:

                # in this json, professor is key and lectures is value
                for professor , lectures in provid_lectures.items():
                    print(f"\nProfessor: {professor}")

                    # because the lectures are list of dict
                    for lecture in lectures:
                        print(f"Lectures: {lecture['name']}, Unit: {lecture['unit']}")
                    

        else:
            print("No lectures provided")
