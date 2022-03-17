"""28. Write a Python program to select
 a string from a given list of strings 
 with the most unique characters. Go to the editor
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
Click me to see the sample solution"""
from utils import  find_uniques, print_my_solution

input_1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
input_2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_28(input_):
    out = ""
    len_ = 0
    for word in input_:
        uniques = find_uniques(word)
        if len(uniques) >= len_:
            len_ = len(uniques)
            out = word
    print(out)

if __name__ == '__main__':
    my_solution_28(inputs)
