from calculating.calc_wo_brackets import calculating_w_out_br
from calculating.brackets_del import brackets

def final(arr):
  br_o = 0
  br_c = 0
  oper = 0
  znaki = ('+', '-', '*', '/', '(', ')', '^')
  znaki_wo_br = ('+', '-', '*', '/', '^')

  # for i in arr:
  #    if i not in znaki:
  #      oper += 1
  # # print(oper)
  # if oper <= 1:
  #    return 'input data error // incorrect symbols or wrong data'
  if '(' in arr:
    for i in arr:
      if i == '(':
        br_o += 1
      elif i == ')':
        br_c += 1
    if br_o != br_c:
      return 'input data error (brackets mismatch)'        
    else:      
      while len(arr) >= 0:  
        arr[arr.index('')]=calculating_w_out_br(brackets(arr))  
        if len(arr) == 1 or len(arr) == 2:  
          return arr[0]
          break   
        return final(arr)
  else:
    if calculating_w_out_br(arr) == 'zero division':
      return calculating_w_out_br(arr)
    else:     
      #return round(calculating_w_out_br(arr),8)
      return calculating_w_out_br(arr)