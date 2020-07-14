current_year=2020
class age_calculation:
    def __init__(self,name,birth_year):
        self.name=name
        self.birth_year=birth_year

    def getAge(self):
        return current_year-self.birth_year

    def __str__(self):
        return '{} age {}'.format(self.name,self.getAge())

class Student(age_calculation):
    def __init__(self,name,birth_year,knowledge):
        age_calculation.__init__(self,name,birth_year)
        self.knowledge=0
    def study(self):
        self.knowledge=self.knowledge+1
    def __str__(self):
        return "{} age {} with points {}".format(self.name,self.getAge(),self.knowledge)
    


donny2=Student('SOURADEEP',1997,0)
print(donny2)
print(donny2.study())
        
