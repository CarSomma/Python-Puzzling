"""27. Write a Python program to find
 x that minimizes mean squared deviation  
 (the mean minimize the mean squared deviation)
from a given a list of numbers. 
Go to the editor
Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142
Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112
Click me to see the sample solution
"""

from utils import print_my_solution

input_1 = [4, -5, 17, -9, 14, 108, -9]
input_2 = [12, -2, 14, 3, -15, 10, -45, 3, 30]
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_27(input_):
    sum_ele = 0 
    len_ = 0

    for num in input_:
        sum_ele += num
        len_ +=1

    avg_ = sum_ele/len_
    print(avg_)

if __name__ == "__main__":
    my_solution_27(inputs)
