
import json




class LectureLimitError(Exception):
    def __init__(self , msg = "Invalid Input. please enter a number between 1 to 5"):
        self.msg = msg
        super().__init__(self.msg)


class ProfessorLecture:
    def __init__(self):
        self.lectures = []

    def read_json(self):
        PATH= "./data/professors_lectures.json"
        try:
        
            with open(PATH , "r") as file:
                return json.load(file)
                
        except:
            return {}
     


    def write_save_json(self , professor_lecture):
        PATH = "./data/professors_lectures.json"
        with open(PATH , "w") as file:
            json.dump(professor_lecture , file , indent=4)
        
        # return professor_lecture
        



    def write_lectures(self , name , family):
        try:

            count_lectures = int(input("Enter the number of lectures: "))
            if (count_lectures < 0 or count_lectures > 5):

                raise LectureLimitError
            
        except ValueError:
            print("Invalid input, please do not enter str. enter int")
            return
        except LectureLimitError as error:
            print(error)
            return
            


        for i in range(count_lectures):
            lectures_name = input(f"Enter the name of lecture {i+1}: ")
            lectures_unit = int(input(f"please Enter the unit of lecture {lectures_name}: "))
            self.lectures.append({"name" : lectures_name , "unit" : lectures_unit})
            
            

        professor_lecture = self.read_json()
        professor_lecture.append({f"{name} {family}" : self.lectures})
        self.write_save_json(professor_lecture)

        # lectures = self.lectures
        # return lectures
    



    # def write_lectures(self , name , family):
    #     try:

    #         count_lectures = int(input("Enter the number of lectures: "))
    #         if (count_lectures < 0 or count_lectures > 5):

    #             raise LectureLimitError
            
    #     except ValueError:
    #         print("Invalid input, please do not enter str. enter int")
    #         return
    #     except LectureLimitError as error:
    #         print(error)
    #         return
            

    #     lectures = []
    #     for i in range(count_lectures):
    #         lectures_name = input(f"Enter the name of lecture {i+1}: ")
    #         lectures_unit = int(input(f"please Enter the unit of lecture {lectures_name}: "))
    #         lectures.append({"name" : lectures_name , "unit" : lectures_unit})
            


    #     professor_lecture = self.read_json()
    #     professor_name = f"{name} {family}"
    #     professor_lecture[professor_name] = lectures
    #     self.write_save_json(professor_lecture)

    #     self.lectures = lectures
    #     return self.lectures