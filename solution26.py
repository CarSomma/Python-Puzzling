"""26. Write a Python program to find
the largest number where commas or periods
are decimal points. Go to the editor
Input:
['100', '102,1', '101.1']
Output:
102.1
Click me to see the sample solution"""

from utils import print_my_solution

input_ = ['100', '102,1', '101.1']
inputs = [input_]

@print_my_solution(inputs)
def my_solution_26(input_):
    max_num = 0
    for str_ in input_:
        num = float(str_.replace(",","."))
        if num>= max_num:
            max_num = num

    print(max_num)

if __name__ == '__main__':
    my_solution_26(inputs)
