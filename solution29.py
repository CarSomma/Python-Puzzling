"""29. Write a Python program to find
the indices of two numbers that sum to 0 
in a given list of numbers. Go to the editor
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
Click me to see the sample solution"""

from utils import print_my_solution

input_1 = [1, -4, 6, 7, 4]
input_2 = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
inputs = [input_1, input_2]

@print_my_solution(inputs)
def my_solution_29(input_):
    out = []
    for idx1, num1 in enumerate(input_):
        for idx2, num2 in enumerate(input_):
            if num1 + num2 == 0:
                    if idx1 not in out and idx2 not in out:
                        out.append(idx1)
                        out.append(idx2)
    print(out) 


if __name__ == '__main__':
    my_solution_29(inputs)