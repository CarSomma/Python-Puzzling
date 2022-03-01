"""5. Write a Python program to check 
the nth-1 string is a proper substring of nth string
 in a given list of strings. Go to the editor
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
input_2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
input_3 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
input_4 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']

inputs = [input_1, input_2, input_3, input_4]

@print_my_solution(inputs)
def my_solution_5(input_):
    second_last_string = input_[-2]
    last_string = input_[-1]
    #print()
    for last_one, second_last in zip([last_string],[second_last_string]):
        
        if len(second_last) > len(last_one):
            print(False)
        else:
            if second_last in last_one:
                print(True)
            else:
                print(False)

if __name__ == "__main__":
    my_solution_5(inputs)