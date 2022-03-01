"""23. Write a Python program to find the indices
for which the numbers in the list drops. 
Go to the editor
NOTE: You can detect multiple drops just by checking
 if nums[i] < nums[i-1]
Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[1, 4, 6, 8, 10, 11, 15, 16, 18]
Input:
[6, 5, 4, 3, 2, 1]
Output:
[1, 2, 3, 4, 5]
Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[0, 2, 4, 6]
Click me to see the sample solution
"""
from numpy import index_exp
from utils import print_my_solution

input_1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
input_2 = [6, 5, 4, 3, 2, 1]
input_3 = [1, 19, 5, 15, 5, 25, 5]
inputs = [input_1,input_2,input_3]

@print_my_solution(inputs)
def my_solution_23(input_):
    indexes = []
    for idx in range(len(input_)):
        if input_[idx] < input_[idx-1]:
            indexes.append(idx)
    print(indexes)


if __name__ == '__main__':
    my_solution_23(inputs)
