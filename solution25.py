"""25. Write a Python program to find the XOR
of two given strings interpreted as binary numbers.
Go to the editor
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
Click me to see the sample solution
"""
from utils import print_my_solution
input_1 = ['0001', '1011']
input_2 = ['100011101100001', '100101100101110']
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_25(input_):
    num = ""
    for first, second in zip(input_[0],input_[1]):
        if first == second:
            num += '0'
        else:
            num += '1'
    print(num)
    int_base2 = int(num,base=2)
    print(bin(int_base2))

if __name__ == '__main__':
    my_solution_25(inputs)
