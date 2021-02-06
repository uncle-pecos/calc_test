from calculating.string_parsing import str_parse
from calculating.finalizing import final
from calculating.str_check import checking



def main_c(inp_str_):   
    temp_arr = str_parse(inp_str_)
    return final(temp_arr)

	
exit = True	
while exit:
	print('Input string \n Input "exit" for exit')
	inp_str = input()
	if inp_str == 'exit':
		exit = False
		break
	else:		
		print(main_c(inp_str))
		print('<-------------------------------->')




