class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'The name of the Pet is {self.name} and his age is {self.age}')

class Cat(Pet):

    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color=color
    def show(self):
        print(f'The name of the Pet is {self.name} and its age is {self.age} anf its color is {self.color}')


    def sound(self):
        print('Meow')
    

class Dog(Pet):
    def sound(self):
        print('bark')

cat=Cat("Sonya",10,'Brown')
cat.show()
