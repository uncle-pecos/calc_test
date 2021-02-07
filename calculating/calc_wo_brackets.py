from calculating.priority import priority
from calculating.return_res import return_res

def calculating_w_out_br(arr):
  #print(arr, '  +  ')  
  st1 = []
  st2 = ['']
  temp = 0
  znaki = ('+', '-', '*', '/', '^')
  #print(arr)
  if '' in arr:
        #print(arr,'---')
        arr.remove('')
        arr.remove('')
        #print(arr,'+')
  #print(arr)    
  if arr == ['=']:
      return 'input data error // incorrect symbols or wrong data'
  #elif len(arr)<3 or (arr[-1] in znaki) :
  #    return 'input data error // not enough data'
  #print(arr,1)
  if len(arr) == 1:
        return arr[0]
  while st2 != []:
    #print(st1,st2,2)
    if st2 == []:
            break
    #print(temp)
    if arr[temp] == '':
          temp += 1
          pass
    elif arr[temp] not in znaki:
      st1.append(arr[temp])
      temp += 1
      #print(st1,st2,3)

    elif arr[temp] in znaki:
      if st2 == []:
            break
      #print(st1,st2,4)
      if priority(arr[temp]) > priority(st2[len(st2)-1]):
        if 'zero division' in st1:
            st1[0] = 'zero division'
            return st1[0]
        if len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
          #st1[0] = return_res(st2[0], st1[0], st1[1] )
          st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-2], st1[len(st1)-1] )
          st1.pop()
        st2.pop()
        st2.append(arr[temp])
        temp += 1
      elif priority(arr[temp]) == priority(st2[len(st2)-1]):
          if len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
             st1[0] = return_res(st2[0], st1[0], st1[1] )
             st1.pop()   
             print(st1,st2,4)
          del st2[0]
          st2.append(arr[temp])
          temp += 1   
      else:
        st2.append(arr[temp])
        temp += 1 
    

    #print(st1,st2,5)
    if st2 == []:
        break
    if temp == len(arr):
      temp_ =  0   
      while st2 != []:
        # if '-' in st2:
        #     if 'zero division' in st1:
        #       st1[0] = 'zero division'
        #       return st1[0]
            # if len(st1) == 1:
            #   break
            
            # # while temp_ <= len(st1)-1:                  
            # #   if priority(st2[temp_]) <= priority(st2[temp_-1]):
            # #     st1[0] = return_res(st2[0], st1[0], st1[1])
            # #     temp_ += 1      
            # #st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-2], st1[len(st1)-1])            
            # del st1[1]
            # del st2[0]
            # #st1.pop()
            # #st2.pop()
            

        # else:
          if len(st2) > 1 and (priority(st2[0]) == priority(st2[1])):
             #print(st1, st2, '??')   
             st1[0] = return_res(st2[0], st1[0], st1[1] )
             del st1[1]
             del st2[0]
          elif len(st1) > 1 and (priority(st2[len(st2)-1])==1 or priority(st2[len(st2)-1])==2 or priority(st2[len(st2)-1])==0):
            #st1[0] = return_res(st2[0], st1[0], st1[1] )
            #print(st1, st2, '??')
            st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-2], st1[len(st1)-1] )
            st1.pop()
            st2.pop()
          # elif len(st2) > 1 and (priority(st2[0]) == priority(st2[1])):
          #    print(st1, st2, '??')   
          #    st1[0] = return_res(st2[0], st1[0], st1[1] )
          #    st1.pop()   
          # st2.pop()
          if st2 == []:
            break
          #print(st1,st2,6)
          if 'zero division' in st1:
            st1[0] = 'zero division'
            return st1[0]
          st1.reverse()
          st2.reverse()
          st1[len(st1)-2] = return_res(st2[len(st2)-1], st1[len(st1)-1], st1[len(st1)-2])
          st1.pop()
          st2.pop()          
          st1.reverse()
          st2.reverse()

          #print(st1,st2,temp)
  #st1.pop('')
  #print(st1, st2, 7)
  try:
    if str(st1[0])[-2:] == '.0' :
      return int(st1[0])
    else:
      return st1[0]
  except:
    return 'input data error // incorrect symbols or wrong data'