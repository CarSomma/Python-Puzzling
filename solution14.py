"""14. Write a Python program to find the lengths
of a given list of non-empty strings. 
Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = ['cat', 'car', 'fear', 'center']
input_2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_14(input_):

    length_out = []
    for word in input_:
        length_out.append(len(word))
    print(length_out)

if __name__ == '__main__':
    my_solution_14(inputs)