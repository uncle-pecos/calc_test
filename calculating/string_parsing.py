def str_parse(inp):
  inp = inp.replace(',','.')
  inp = inp.replace('(-','(0-')
  inp = inp.replace('((','(1*(')
  inp = inp.replace('(((','(1*(1*(')    
  #inp = inp.replace('(','1*(')  
  #print(inp)
  if inp[0] == '-':
    inp = inp[:0] + '0' + inp[0:]
  temp_arr = ['']
  i = 0
  j = 0
  znaki = ('+', '-', '*', '/', '(', ')')
  try:
    while i<len(inp):
      while i<len(inp) and inp[i] in znaki:      
        temp_arr[j] += inp[i]
        i += 1
        j += 1
        temp_arr.append('')
        if i>=len(inp):
          break
         
      while i<len(inp) and inp[i] not in znaki:
       temp_arr[j] += inp[i]
       i += 1 
       if i>=len(inp):
         break 
      if i>=len(inp):
        break                        
      temp_arr[j] = float(temp_arr[j])
      temp_arr.append('')
      j += 1
      if i>=len(inp):
        break          
    for m in temp_arr:
      if m == '':
        temp_arr.remove('')  
    if temp_arr[-1] not in znaki:
       temp_arr[-1]=float(temp_arr[-1])
    #print(temp_arr)        
    return temp_arr
  except:
    temp_arr = ['=']
    return temp_arr 