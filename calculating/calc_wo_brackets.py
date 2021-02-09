from calculating.priority import priority
from calculating.return_res import return_res

def calculating_w_out_br(arr):
  st1 = []
  st2 = ['']
  temp = 0
  znaki = ('+', '-', '*', '/', '^')

  if '' in arr:                                                         #убираем из массива лишние пустые элементы
        arr.remove('')
        arr.remove('')
   
  if arr == ['=']:
      return 'input data error // incorrect symbols or wrong data'

  if len(arr) == 1:
        return arr[0]
  while st2 != []:

    if st2 == []:
            break

    if arr[temp] == '':
          temp += 1
          pass
    elif arr[temp] not in znaki:
      st1.append(arr[temp])
      temp += 1


    elif arr[temp] in znaki:
      if st2 == []:
            break

      if priority(arr[temp]) > priority(st2[len(st2)-1]):                           #заполняем стек в зависимости от приоритета знака
        if 'zero division' in st1:
            st1[0] = 'zero division'
            return st1[0]
        elif 'Result too large' in st1:
            st1[0] = 'Result too large'
            return st1[0] 
        if len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
          st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-2], st1[len(st1)-1] )
          st1.pop()
        st2.pop()
        st2.append(arr[temp])
        temp += 1
      elif priority(arr[temp]) == priority(st2[len(st2)-1]):                                                                      
          if len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
             st1[0] = return_res(st2[0], st1[0], st1[1] )
             st1.pop()   
          del st2[0]
          st2.append(arr[temp])
          temp += 1   
      else:
        st2.append(arr[temp])
        temp += 1 
    
   
    if st2 == []:
        break
    if temp == len(arr):
      temp_ =  0   
      while st2 != []:
          if 'zero division' in st1:
            st1[0] = 'zero division'
            return st1[0]
          elif 'Result too large' in st1:
            st1[0] = 'Result too large'
            return st1[0] 

          if len(st2) > 1 and (priority(st2[0]) == priority(st2[1])):
  
             st1[0] = return_res(st2[0], st1[0], st1[1] )
             del st1[1]
             del st2[0]
          elif len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
            st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-2], st1[len(st1)-1] )
            st1.pop()
            st2.pop()

          if st2 == []:
            break

          if 'zero division' in st1:
            st1[0] = 'zero division'
            return st1[0]
          elif 'Result too large' in st1:
            st1[0] = 'Result too large'
            return st1[0]  
          st1.reverse()
          st2.reverse()
          st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-1], st1[len(st1)-2])
          st1.pop()
          st2.pop()          
          st1.reverse()
          st2.reverse()

  try:
    if str(st1[0])[-2:] == '.0' :
      return int(st1[0])
    else:
      return st1[0]
  except:
    return 'input data error // incorrect symbols or wrong data'