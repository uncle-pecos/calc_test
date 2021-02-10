import unittest
from . import *
from calculating.str_check import checking
from calculating.string_parsing import str_parse
from calculating.calc_wo_brackets import calculating_w_out_br
from calculating.brackets_del import brackets


class TestUnits(unittest.TestCase):
    
    def test_str_check_bad(self):
        str = ['((', '()', '-', '1++1', 'abc', '', '1+a', '1+1a', ' ']
        for i in str:
            print(i, '   Tested ok ++++')
            self.assertEqual(checking(i), False)

    def test_str_check_good(self):
        str = ['1+2', '(1+2)', '1+2*2', '1', '(3+(2*3)-4)', '2^(3-3)', '1+4/5-8+4^0.543', '5^0*(2^14)']
        for i in str:
            print(i, '  Tested ok ++++')
            self.assertEqual(checking(i), i)            

    def test_str_check(self):
        str1 = '(((14-2)))'
        str2 = '-1'
        str3 = '-(-1,9)'
        str4 = '-((13+3   ))+(-12+4)'
        self.assertEqual(checking(str1), '(1*(1*(14-2)))')
        self.assertEqual(checking(str2), '0-1')
        self.assertEqual(checking(str3), '0-(0-1.9)')  
        self.assertEqual(checking(str4), '0-(1*(13+3))+(0-12+4)')  

    def test_str_parse(self):
        str1 = '1'
        str2 = '1+4'
        str3 = '(1.4+4)'
        str4 = '(1*4)-(13^3^3)'
        self.assertEqual(str_parse(str1), [1.0])
        self.assertEqual(str_parse(str2), [1, '+', 4.0])
        self.assertEqual(str_parse(str3), ['(', 1.4, '+', 4.0, ')'])
        self.assertEqual(str_parse(str4), ['(', 1.0, '*', 4.0, ')', '-', '(', 13.0, '^', 3.0, '^', 3.0, ')'])

    def test_calc(self):
        arr1 = [1.0]
        arr2 = [1.0, '+', 4.0]
        arr3 = [13.0, '^', 3.0, '^', 3.0]
        arr4 = [15.543, '/', 15.0, '*', 1.0]
        arr5 = [15.0, '-', 7.0, '*', 2.0]
        self.assertEqual(calculating_w_out_br(arr1), 1)
        self.assertEqual(calculating_w_out_br(arr2), 5)
        self.assertEqual(calculating_w_out_br(arr3), 10604499373)
        self.assertEqual(calculating_w_out_br(arr4), 1.0362)
        self.assertEqual(calculating_w_out_br(arr5), 1)

    def test_del_brackets(self):
        arr1 = ['(', 1.0, '*', 4.0, ')', '-', '(', 13.0, '^', 3.0, '^', 3.0, ')']
        arr2 = ['(', '(', 1.0, '*', 4.0, ')', '+', 15.0, ')']
        arr3 = [3.0, '-', 14.4, '+', '(', 0, '-', 13.9, '*', '(', 1.0, '-', 1.0, '*', 5.9, ')', ')' ]
        arr4 = ['(', -14.5, '(', '(', 14.0, '+', 0.1, ')', '-', 0, ')', ')']
        self.assertEqual(brackets(arr1), [1.0, '*', 4.0])
        self.assertEqual(brackets(arr2), [1.0, '*', 4.0])
        self.assertEqual(brackets(arr3), [1.0, '-', 1.0, '*', 5.9])
        self.assertEqual(brackets(arr4), [14.0, '+', 0.1])
        

if __name__ == '__main__':
    unittest.main()