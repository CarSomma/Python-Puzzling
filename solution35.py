"""35. Write a Python program to compute
 the product of the odd digits in a given number, 
 or 0 if there aren't any. Go to the editor
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = str(123456789)
input_2 = str(2468)
input_3 = str(13579)
inputs = [input_1, input_2, input_3]

@print_my_solution(inputs)
def my_solution_35(input_):
    odd_digits = []
    for digit in input_:
        int_digit = int(digit)
        if int_digit % 2 == 1:
            odd_digits.append(int_digit)

    if len(odd_digits) !=0:
        product = 1
        for odd in odd_digits:
            product *= odd
        print(product)
    else:
        print(0)#

if __name__ == '__main__':
    my_solution_35(inputs)

    



