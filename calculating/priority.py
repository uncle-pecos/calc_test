def priority(znak):
    if znak == '*' or znak =='/':
        return 1
    elif znak == '+' or znak == '-':
        return 2
    elif znak == '^':
        return 0
    else:
        return -10