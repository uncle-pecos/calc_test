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
      while len(arr) >= 0:
        try:
          arr[arr.index('')]=calculating_w_out_br(brackets(arr))          #заменяем выражение в скобках одним полученным числом  
          if len(arr) == 1 or len(arr) == 2:  
            return arr[0]
            break   
          return final(arr)                                               #повторяем подсчет, пока не закончатся скобки
        except:
          return 'input data error // incorrect symbols or wrong data'  
  else:
      return calculating_w_out_br(arr)                                    #если скобок нет, то считаем без них