"""
Here, like the Professors class, we have created a class for the Students, which inherits from the Persons class,
and the init function contains the attributes for the student, and then we have created a function 
to show the student information, student_show_info(), and inside this function, 
the person class show function is also called, show_info()
"""

from src.person import Persons

class Students(Persons):
    
    def __init__(self, pers_id, name, family, gender, year_of_birth , entry_year , student_id):
        super().__init__(pers_id, name, family, gender, year_of_birth)

        self.entry_year = entry_year
        self.student_id = student_id


    def student_show_info(self):
        self.show_info()
        print(f"Student ID: {self.student_id},\tEntry year: {self.entry_year}")
        print()
        print(50*"-")
