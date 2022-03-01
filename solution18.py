"""18. An irregular/uneven matrix, or ragged matrix,
is a matrix that has a different number of elements in each row.
Ragged matrices are not used in linear algebra,
since standard matrix transformations cannot be performed on them,
but they are useful as arrays in computing.
Write a Python program to find the indices
of all occurrences of target in the uneven matrix. Go to the editor
Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [19, 35, 4], [3, 19]),19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]]
Click me to see the sample solution
"""
from utils import print_my_solution
input_1 = [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
input_2 = [([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_18(input_):
    target = input_[1]
    num_lists_tuple = input_[0]

    output = []
    for index_list, num_list in enumerate(num_lists_tuple):
        if target in num_list:
            for index_target, number in enumerate(num_list):
                if number == target:
                    output.append([index_list,index_target])

    print(output)

if __name__ == "__main__":
    my_solution_18(inputs)