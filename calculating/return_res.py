from calculating.calc_main import result

def return_res(znak,a,b):
    if znak == '+':
        return result.plus(a,b)
    elif znak == '-':
        return result.minus(a,b)
    elif znak == '*':
        return result.mult(a,b)
    elif znak == '/':
        return result.divis(a,b) 