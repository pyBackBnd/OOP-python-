class People:
    number_of_people=0
    def __init__(self,name):
        self.name=name
        People.add_person()

    @classmethod    
    def number_of_people_(cls): #it does not acting with instances. this is meant to be a class method. It is just acting on this class
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1 
        

p1=People('Dmitrii')
print(p1.name,p1.number_of_people)
print(People.number_of_people_())