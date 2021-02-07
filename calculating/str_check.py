def checking(inp):
  inp = inp.replace(' ', '')
  inp = inp.replace(',', '.')
  oper = 0
  operands = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.')
  znaki = ('+', '-', '*', '/', '^','(', ')')

  for m in inp:
     if m in operands:
       oper += 1
  if oper == 0:
     return False

  for m in inp:
    if m not in znaki and m not in operands:
        return False  


  znaki_wo_br = ('+', '-', '*', '/', '^')
  znaki_wo_min = ('+', '/', '*')
  #znaki_wo_mult = ('+', '/', '-', '^')
  inp = inp.replace('(-','(0-')
  inp = inp.replace('((','(1*(')
  inp = inp.replace('(((','(1*(1*(')    
  #print(inp)
  if inp[0] == '-' and (inp[1] in operands or inp[1] == '('):
    if len(inp) >= 2:
      inp = inp[:0] + '0' + inp[0:]
  
  if inp[len(inp)-1] in znaki_wo_br or inp[len(inp)-1] == '(':
          return False

  count = 0
  for m in inp:
        if m =='(':
              count +=1
  if count >= 2:
      for m in range(1,len(inp)-1): 
              if inp[m] == '(' and inp[m-1] not in znaki_wo_br:
                    return False  
  

  if inp[0] != '(':
        for m in range(len(inp)-1): 
              if inp[m] == '(' and inp[m-1] not in znaki_wo_br:
                    return False 


  if len(inp)>=3:
        for m in range(len(inp)-1): 
          if inp[m] == '(' and inp[m+1] in znaki_wo_min:
            return False
          elif inp[m] in znaki_wo_br and (inp[m+1] in znaki_wo_br or inp[m+1] == ')'):               
            return False
          elif inp[m] in operands and inp[m+1] == '(':
            return False
          #elif inp[m] == ')' and  inp[m+1] in operands:
          #  return False     
        return inp 
  else:
      return inp            


  