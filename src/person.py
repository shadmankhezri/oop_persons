"""

"""



from datetime import date

class Persons:
    def __init__(self , pers_id , name , family , gender , year_of_birth):
        self.pers_id = pers_id
        self.name = name
        self.family = family
        self.gender = gender
        self.year_of_birth = year_of_birth


    def calculate_age(self):
        try:
            current_year = date.today().year
            return (current_year - self.year_of_birth)
        
        except Exception as error:
            print(f"\nError calculating age:{error}\npleas input int for year_of_birth\n")

    

    def show_info(self):
        print(50*"-")
        print("\nInformations:\n")
        print(f"National ID: {self.pers_id},\tName: {self.name},\tFamily: {self.family},\tGender: {self.gender},\tAge: {self.calculate_age()}")
        