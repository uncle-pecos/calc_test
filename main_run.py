from calculating.string_parsing import str_parse
from calculating.finalizing import final

inp_str = str(input())
temp_arr = str_parse(inp_str)
print(final(temp_arr))



