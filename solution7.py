"""7. Write a Python program to check
 a given list of integers where the sum
of the first i integers is i. Go to the editor
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = [0, 1, 2, 3, 4, 5]
input_2 = [1, 1, 1, 1, 1, 1]
input_3 = [2, 2, 2, 2, 2]
inputs = [input_1, input_2, input_3]

@print_my_solution(inputs)
def my_solution_7(input_):
    sum_ = 0
    for idx, num in enumerate(input_):
        sum_ += num
        if sum_ > len(input_):
            print(False)
            break
        elif sum_ == len(input_) and idx == len(input_) -1:
            print(True)

if __name__ == '__main__':
    my_solution_7(inputs)