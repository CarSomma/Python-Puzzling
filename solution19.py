"""19. Write a Python program to split a given string (s)
into strings if there is a space in the string,
otherwise split on commas if there is a comma,
otherwise return the list of lowercase letters with odd order
(order of a = 0, b = 1, etc.) Go to the editor
Input:
a b c d
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma, 
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma, 
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string, 
otherwise split on commas if there is a comma,
Output:
['b', 'd']
Click me to see the sample solution"""
import re
from utils import print_my_solution
input_1 = "a b c d"
input_2 = "a,b,c,d"
input_3 = "abcd"
inputs = [input_1,input_2,input_3]

@print_my_solution(inputs)
def my_solution_19(input_):
    if " " in input_ or "," in input_:
        print(re.split(r"[, ]",input_))
    else:
        ch_list = []
        for ch in input_:
            ch_list.append(ch)
        print(ch_list)

if __name__ == '__main__':
    my_solution_19(inputs)