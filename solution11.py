"""11. Write a Python program to find
the indexes of numbers of a given list
 below a given threshold. Go to the editor
Input:
[(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
Output:
[0, 1, 2, 3, 7, 8, 9, 10]
Input:
[(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
Output:
[0, 2, 3, 5, 6, 7, 8]
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
input_2 = [(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
inputs = [input_1, input_2]
@print_my_solution(inputs)
def my_solution_11(input_):
    threshold = input_[0][0]
    number_tuple = input_[0][1]

    indexes = []
    for index, num in enumerate(number_tuple):
        if num < threshold:
            indexes.append(index)
    print(indexes)

if __name__ == '__main__':
    my_solution_11(inputs)