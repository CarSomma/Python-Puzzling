"""22. Write a Python program to compute 
the sum of the ASCII values of the upper-case 
characters in a given string. Go to the editor
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = "PytHon ExerciSEs"
input_2 = "JavaScript"
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_22(input_):
    sum_ascii = 0
    for ch in input_:
        if ch.isupper():
            ascii_value = ord(ch)
            sum_ascii += ascii_value
    print(sum_ascii)

if __name__ == '__main__':
    my_solution_22(inputs)