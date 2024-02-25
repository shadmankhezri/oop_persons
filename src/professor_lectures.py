"""
In this module we have first created a custom class LectureLimitError to receive the error.
Then we have class ProfessorLecture, which we have created the related object in module professor_menu, 
and there are functions related to creating lectures that can be presented by professors, as well as storing them.

Saving lectures is done in such a way that the professor first specifies the number of lectures 
he wants to provid. But we have created a limit for the professors, that is, they cannot provided 
more than 5 lectures. 
And to save the lectures, first the json file related to the provided lectures is read and then the 
lessons are added to the end of that json.

"""


import json

class LectureLimitError(Exception):
    def __init__(self , msg = "Invalid Input. please enter a number between 1 to 5"):
        self.msg = msg                      
        super().__init__(self.msg)             # if the professors want provid lectures more than 5


class ProfessorLecture:
    def __init__(self):
        self.lectures = []


    def read_json(self):
        PATH= "./data/professors_lectures.json"

        try:                                 
            with open(PATH , "r") as file:   # If there is a Json file in that path, it will be returned
                return json.load(file)
                
        except:
            return {}                       # if not exist , {} will be returned
     



    def write_save_json(self , professor_lecture):
        PATH = "./data/professors_lectures.json"
        
        with open(PATH , "w") as file:
            json.dump(professor_lecture , file , indent=4)
        
        



    def write_lectures(self , name , family):        # when the professors want provided lectures in menu called it
        try:
            count_lectures = int(input("Enter the number of lectures: "))

            if (count_lectures < 0 or count_lectures > 5):
                raise LectureLimitError
            

        except ValueError:                            # if in the count_lectures input string
            print("Invalid input, please do not enter str. enter int")
            return                                    # for return to the professor menu
        
        
        except LectureLimitError as error:            # if input num more than 5
            print(error)
            return                                    # for return to the professor menu
            

        # when every thing was true , then runed this part 
        for i in range(count_lectures):

            lectures_name = input(f"Enter the name of lecture {i+1}: ")
            lectures_unit = int(input(f"please Enter the unit of lecture {lectures_name}: "))

            # make the list of dict in the self.lectures
            self.lectures.append({"name" : lectures_name , "unit" : lectures_unit})
            
            
        # call defs with the object professor_lecture
            
        professor_lecture = self.read_json()
        professor_lecture.append({f"{name} {family}" : self.lectures})
        self.write_save_json(professor_lecture)

