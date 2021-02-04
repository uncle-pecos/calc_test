class Calc:
    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mult(self, a, b):
        return a*b 

    def divis(self, a, b):
        if b==0:
            return 'zero division'
        else:
            return a/b

    def step(self, a, b):
        return a**b

result = Calc()