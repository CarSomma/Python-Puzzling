"""17. Write a Python program to create string
consisting of the non-negative integers up to n inclusive.
Go to the editor
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Click me to see the sample solution"""

from utils import print_my_solution

input_1 = 4
input_2 = 15
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_17(input_):

    str_out = ""
    for num in range(input_+1):
        str_out += str(num) + " "
    print(str_out)

if __name__ == "__main__":
    my_solution_17(inputs)
