from calculating.str_check import checking

def str_parse(inp):                               #превращаем готовую строку в массив
  znaki = ('+', '-', '*', '/', '^','(', ')')
  temp_arr = ['']
  if checking(inp) == False:     
     temp_arr = ['=']
     return temp_arr 
  else:
    inp = checking(inp)        
  i = 0
  j = 0

  try:
    while i<len(inp):   
      while i<len(inp) and inp[i] in znaki:           #если это операция, то просто добавляем его в массив
        temp_arr[j] += inp[i]
        i += 1
        j += 1
        temp_arr.append('')
        if i>=len(inp):
          break
         
      while i<len(inp) and inp[i] not in znaki:      #если это число, то плюсуем строку
       temp_arr[j] += inp[i]
       i += 1 
       if i>=len(inp):
         break 
      if i>=len(inp):
        break                        
      temp_arr[j] = float(temp_arr[j])                #переводим полученное число в тип float
      temp_arr.append('')
      j += 1
      if i>=len(inp):
        break          
    for m in temp_arr:
      if m == '':
        temp_arr.remove('')  
    if temp_arr[-1] not in znaki:
       temp_arr[-1]=float(temp_arr[-1])         
    return temp_arr
  except:
    temp_arr = ['=']
    return temp_arr 