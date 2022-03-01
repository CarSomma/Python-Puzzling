"""21. Write a Python program to check, 
for each string in a given list, 
whether the last character is an isolated letter or not.
 Return True or False. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = ['cat', 'car', 'fear', 'center']
input_2 = ['ca t', 'car', 'fea r', 'cente r']
inputs = [input_1, input_2]

@print_my_solution(inputs)
def my_solution_21(input_):
    out_list = []
    for word in input_:
        if word[-2] == " ":
            out_list.append(True)
        else:
            out_list.append(False)
    print(out_list)

if __name__ == "__main__":
    my_solution_21(inputs)