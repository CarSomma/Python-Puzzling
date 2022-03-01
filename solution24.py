"""24. Write a Python program to create
 a list whose ith element is the maximum
 of the first i elements from a input list. Go to the editor
Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
Input:
[6, 5, 4, 3, 2, 1]
Output:
[6, 6, 6, 6, 6, 6]
Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[1, 19, 19, 19, 19, 25, 25]
Click me to see the sample solution"""
from utils import print_my_solution
input_1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
input_2 = [6, 5, 4, 3, 2, 1]
input_3 = [1, 19, 5, 15, 5, 25, 5]
inputs = [input_1, input_2, input_3]

@print_my_solution(inputs)
def my_solution_24(input_):
    out_ith_max = []
    max_num = 0
    for num in input_:
        if num >= max_num:
            max_num = num
            out_ith_max.append(num)
        else:
            out_ith_max.append(max_num)

    print(out_ith_max)

if __name__ == '__main__':
    my_solution_24(inputs)