"""34. Write a Python program to find 
the sum of the numbers of a given list 
among the first k with more than 2 digits. Go to the editor
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 4
Output:
0
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 6
Output:
108
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 5
Output:
331
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 1
Output:
114
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = (4,[4, 5, 17, 9, 14, 108, -9, 12, 76])
input_2 = (6,[4, 5, 17, 9, 14, 108, -9, 12, 76])
input_3 = (5,[114, 215, -117, 119, 14, 108, -9, 12, 76])
input_4 = (1,[114, 215, -117, 119, 14, 108, -9, 12, 76])

inputs = [input_1, input_2, input_3, input_4]

@print_my_solution(inputs)
def my_solution_34(input_):

    first_ks = input_[0]
    list_nums = input_[1]

    sum_ = 0
    for num in list_nums[:first_ks]:
        if num > 99 or num < -99:
                sum_ += num
    print(sum_)

if __name__ == "__main__":
    my_solution_34(inputs)