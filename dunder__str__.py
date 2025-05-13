class CastomizedInteger:
    def __init__(self,integer):
        self.integer=integer
    
    def __str__(self):
        if self.integer==6:
            return 'Six'

    def __repr__(self):
        return f'CustomizedInteger({self.integer})'


x=CastomizedInteger(6)
print(x)
        