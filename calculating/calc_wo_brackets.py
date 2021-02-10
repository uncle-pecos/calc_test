from calculating.priority import priority
from calculating.return_res import return_res

def calculating_w_out_br(arr):                                          #считаем выражение без скобок с помощью двойного стека
  st1 = []
  st2 = []
  temp = 0
  znaki = ('+', '-', '*', '/', '^')
   
  if arr == ['=']:                                                      #если после парсинга строки нам пришел массив [=], то выводим ошибку
      return 'input data error // incorrect symbols or wrong data'

  if len(arr) == 1:                                                     #если длина массива - один элемент, то его и возвращаем  
        return arr[0]      

  for i in arr:                                                         #разбиваем массив на числа и знаки
      if i in znaki:
          st2.append(i)
      else:
          st1.append(i)         
  
  while st2 != []:                                                      #считаем, пока не освободим массив с операциями 
      if 'Result too large' in st1:
          return 'Result too large'
      elif 'zero division' in st1:
          return 'zero division'       
      if len(st2) != 1:
        try:
          if priority(st2[temp+1])>=priority(st2[temp]):                  
            st1[temp] = return_res(st2[temp], st1[temp], st1[temp+1])
            del st2[temp]
            del st1[temp+1]
            temp = 0   
          else:
            temp += 1
        except:
          if priority(st2[temp])<=priority(st2[temp-1]):
            st1[temp] = return_res(st2[temp], st1[temp], st1[temp+1]) 
            del st2[temp]
            del st1[temp+1]
            temp = 0     

      elif len(st2) == 1:
          st1[0] = return_res(st2[0], st1[0], st1[1])
          del st2[0]
          del st1[1]    

  try:
    if str(st1[0])[-2:] == '.0' :                                         #переводим обратно в int, если это возможно
      return int(st1[0])
    else:
      return st1[0]
  except:
    return 'input data error // incorrect symbols or wrong data'