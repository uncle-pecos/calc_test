def brackets(br_array):
  i = 0
  br_array_l = []
  while i < len(br_array):
    if br_array[i] == ')':                                  #идем по массиву, пока не найдем закрывающую скобку
      temp_c = br_array.index(br_array[i])                                            
      break    
    i += 1

  while br_array[i] != '(':                                 #идем обратно по массиву, пока не найдем открывающую скобку
    i -= 1
    temp_o = i 
  

  j = temp_o
  while j <= temp_c:
      br_array_l.append(br_array[j])                        
      br_array[j] = ''
      j += 1
  for m in br_array:
    if m == '':
      br_array.remove('')
      br_array.remove('')
  if len(br_array_l[1:len(br_array_l)-1]) == 1:
    br_array_l.pop()
    br_array_l.append('-')
    br_array_l.append(0)
    br_array_l.append(')')
  return br_array_l[1:len(br_array_l)-1]