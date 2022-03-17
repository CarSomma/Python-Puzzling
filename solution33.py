"""33. Write a Python program to find
the positions of all uppercase vowels (not counting Y)
in even indices of a given string. Go to the editor
Input: w3rEsOUrcE 
Output:
[6]
Input: AEIOUYW 
Output:
[0, 2, 4]
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = "w3rEsOUrcE"
input_2 = "AEIOUYW"
inputs = [input_1, input_2]

@print_my_solution(inputs)
def my_solution_33(input_):
    out = []
    for idx, ch in enumerate(input_):
        if idx % 2 == 0 and ch in "AEIOU" and ch != 'Y':
            out.append(idx)
    print(out)


if __name__ == '__main__':
    my_solution_33(inputs)

