from calculating.string_parsing import str_parse
from calculating.finalizing import final
from calculating.str_check import checking



def main_c(inp_str_):   
    temp_arr = str_parse(inp_str_)
    return final(temp_arr)

inp_str = input()
print(main_c(inp_str))



