"""20. Write a Python program to determine 
the direction ('increasing' or 'decreasing')
of monotonic sequence numbers. Go to the editor
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = [1, 2, 3, 4, 5, 6]
input_2 = [6, 5, 4, 3, 2, 1]
input_3 = [19, 19, 5, 5, 5, 5, 5]
inputs = [input_1, input_2, input_3]

@print_my_solution(inputs)
def my_solution_20(input_):
    shifted_input = input_[1:]
    increasing_print = []
    decreasing_print = []
    for first, second in zip(input_, shifted_input):
        if first == second:
            print("Not a monotonic sequence!")
            break
        else:
            if second -first == 1:
                increasing_print.append(1)
            elif second - first == -1:
                decreasing_print.append(1)

    if increasing_print.count(1) == len(input_) -1:
        print('increasing')
    elif decreasing_print.count(1) == len(input_) -1:
        print('decreasing')

if __name__ == '__main__':
    my_solution_20(inputs)

