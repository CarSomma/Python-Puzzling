"""3. Write a Python program that accept an integer
 test whether an integer greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True

Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = 922
input_2 = 914
input_3 = 854

inputs = [input_1, input_2, input_3]

@print_my_solution(inputs)
def my_solution_3(num1, num2:int, dividend:int):
    if num1 < num2**num2:
        print(False)
    else:
        if num1%dividend == num2:
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    my_solution_3(inputs, num2=4, dividend=34)