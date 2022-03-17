"""36. Write a Python program to find
the largest k numbers
from a given list of numbers. Go to the editor
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4]
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
Output:
[6, 5, 5, 4, 3]
Click me to see the sample solution
"""

from utils import print_my_solution_2
input_ = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k_list = [1, 2, 3, 4, 5]

@print_my_solution_2(k_list,input_)
def my_solution_36(input_,k):
    desc_input = sorted(input_,reverse=True)
    top_k = desc_input[:k]
    print(top_k)


if __name__ == '__main__':
    my_solution_36(input_,k_list)