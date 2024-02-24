
from src.person import Persons


class Professors(Persons):

    def __init__(self, pers_id, name, family, gender, year_of_birth , professor_id , rank):
        super().__init__(pers_id, name, family, gender, year_of_birth)

        self.professor_id = professor_id
        self.rank = rank



    def professor_show_info(self):
        self.show_info()
        print(f"Professor ID: {self.professor_id},\tRank: {self.rank}")



    