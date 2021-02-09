class Calc:
    def plus(self, a, b):
        try:
            return a + b
        except OverflowError:
            return 'Result too large'

    def minus(self, a, b):
        return a - b

    def mult(self, a, b):
        try:
            return a*b 
        except OverflowError:
            return 'Result too large'

    def divis(self, a, b):
        try:
            if b==0:
                return 'zero division'
            else:
                return a/b
        except OverflowError:
            return 'Result too large'        

    def step(self, a, b):
        try:
            return a**b
        except OverflowError:
            return 'Result too large'

result = Calc()