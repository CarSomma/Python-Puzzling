"""13. Write a Python program to find 
the strings in a given list, starting 
with a given prefix. Go to the editor
Input:
[( 'ca',('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = [( 'ca',('cat', 'car', 'fear', 'center'))]
input_2 = [('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_13(input_):
    prefix = input_[0][0]
    string_tuple = input_[0][1]

    string_out = []
    for string in string_tuple:
        if string.startswith(prefix):
            string_out.append(string)

    print(string_out)

if __name__ == "__main__":
    my_solution_13(inputs)

