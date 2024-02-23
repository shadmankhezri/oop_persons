
from src.person import Persons


class Professors(Persons):

    def __init__(self, pers_id, name, family, gender, year_of_birth , prof_id , rank):
        super().__init__(pers_id, name, family, gender, year_of_birth)

        self.prof_id = prof_id
        self.rank = rank



    def professor_show_info(self):
        self.show_info()
        print(f"Professor ID: {self.prof_id},\tRank: {self.rank}")



    