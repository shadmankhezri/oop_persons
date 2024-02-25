"""
In this module, we have created a class for Professor that inherits from Persons. 
And then we have created a function to show its information, def professor_show_info()
which also calls the function to show the information of class Persons, def show_info()
"""

from src.person import Persons


class Professors(Persons):
                                     # The init function includes the required attributes
    def __init__(self, pers_id, name, family, gender, year_of_birth , professor_id , rank):
        super().__init__(pers_id, name, family, gender, year_of_birth)     
                                        # To indicate inheritance from the Person class

        self.professor_id = professor_id
        self.rank = rank



    def professor_show_info(self):
        self.show_info()                    # call this def from Person class
        print(f"Professor ID: {self.professor_id},\tRank: {self.rank}")



    