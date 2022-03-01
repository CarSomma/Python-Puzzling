"""9. Write a Python program to find list integers
 containing exactly four distinct values, such that
no integer repeats twice consecutively among the first
 twenty entries. Go to the editor
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
Click me to see the sample solution
"""
from utils import print_my_solution, find_uniques

input_1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
input_2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
input_3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
inputs = [input_1,input_2,input_3]

# print(len(set(input_1)))

@print_my_solution(inputs)
def my_solution_9(input_):

    uniques = find_uniques(input_)
    if len(uniques)!= 4:
        print(False)
    else:
        shifted_input = input_[1:]
        different_couple = []
        for first_num, second_num in zip(input_,shifted_input):
            if first_num != second_num:
                different_couple.append('yes')
            else:
                break
        
        if len(different_couple)+1 == len(input_):
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    my_solution_9(inputs)
