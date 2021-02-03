def priority(znak):
    if znak == '*' or znak =='/':
        return 1
    elif znak == '+' or znak == '-':
        return 2
    else:
        return -10