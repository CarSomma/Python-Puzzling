"""37. Write a Python program
to find the largest integer divisor of a number
n that is less than n. Go to the editor
Input: 18
Output:
9
Input: 100
Output:
50
Input: 102
Output:
51
Input: 500
Output:
250
Input: 1000
Output:
500
Input: 6500
Output:
3250
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = 18
input_2 = 100
input_3 = 102
input_4 = 500
input_5 = 1000
input_6 = 6500

inputs = [input_1, input_2, input_3, input_4, input_5, input_6]

@print_my_solution(inputs)
def my_solution_37(input_):

    if input_ % 2 == 0:
        print(input_//2)

if __name__ == '__main__':
    my_solution_37(inputs)