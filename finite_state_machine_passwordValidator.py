from enum import Enum

class States(Enum):
    true=True
    false=False

class PassworsValidator:

    def __init__(self,passwrd:str):
        self.passwrd=passwrd
        self.letter=States.false
        self.digit=States.false
        self.transition()
    def transition(self):
        for i in self.passwrd:
            if i.isalpha():
                self.letter=States.true
            elif i.isdigit():
                self.digit=States.true
    def validate(self):
        if self.digit.value and self.letter.value:
            return True
        else:
            return False
    def __str__(self):
        return self.passwrd
    

passw=PassworsValidator('as1')

print(passw.validate())

