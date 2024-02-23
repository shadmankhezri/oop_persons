

from src.person import Persons

class Students(Persons):
    def __init__(self, pers_id, name, family, gender, year_of_birth , entry_year , student_id):
        super().__init__(pers_id, name, family, gender, year_of_birth)

        self.entry_year = entry_year
        self.student_id = student_id


    def student_show_info(self):
        self.show_info()
        print(f"Student ID: {self.student_id},\tEntry year: {self.entry_year}")
