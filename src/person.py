"""
Within Person class, which is considered the parent, in the init function, features that are common 
to all persons are included, such as name, family, age, etc. And then we have created a function to 
calculate the age of the person, calculate_age(). in such a way that we enter the year of birth for 
the person and this function calculates the age of the person based on the year of birth and inside 
the function related to show the information it shows the age of the person instead of the year of birth

"""


# import this for calculate age
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
            current_year = date.today().year      # separate the year from the current date
            return (current_year - self.year_of_birth)
        
        # If enter the year of birth as a string, this line will be executed and it will show None 
        # the information inside the display function
        except Exception as error:
            print(f"\nError calculating age:{error}\npleas input int for year_of_birth\n")

    

    def show_info(self):
        print(50*"-")
        print("\nInformations:\n")
        print(f"National ID: {self.pers_id},\tName: {self.name},\tFamily: {self.family},\tGender: {self.gender},\tAge: {self.calculate_age()}")
        