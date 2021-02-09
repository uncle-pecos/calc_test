from calculating.calc_wo_brackets import calculating_w_out_br
from calculating.brackets_del import brackets

def final(arr):
  br_o = 0
  br_c = 0
  oper = 0
  count = 0
  znaki = ('+', '-', '*', '/', '(', ')', '^')
  znaki_wo_br = ('+', '-', '*', '/', '^')

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
        try:
          arr[arr.index('')]=calculating_w_out_br(brackets(arr))
          if len(arr) == 1 or len(arr) == 2:  
            return arr[0]
            break   
          return final(arr)
        except:
          return 'input data error // incorrect symbols or wrong data'  
  else:
    if calculating_w_out_br(arr) == 'zero division' or calculating_w_out_br(arr) == 'Result too large':
      return calculating_w_out_br(arr)
    else:  
      return calculating_w_out_br(arr)