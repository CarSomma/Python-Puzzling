"""32. Write a Python program to rescale
and shift numbers of a given list, so that they cover the range [0, 1]. Go to the editor
Input:
[18.5, 17.0, 18.0, 19.0, 18.0]
Output:
[0.75, 0.0, 0.5, 1.0, 0.5]
Input:
[13.0, 17.0, 17.0, 15.5, 2.94]
Output:
[0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]
Click me to see the sample solution
"""
from utils import print_my_solution
input_1 = [18.5, 17.0, 18.0, 19.0, 18.0]
input_2 = [13.0, 17.0, 17.0, 15.5, 2.94]
inputs = [input_1,input_2]

@print_my_solution(inputs)
def my_solution_32(input_):
    min_ = min(input_)
    max_ = max(input_)
    out = []
    for ele in input_:
        new_ele = (ele - min_)/(max_ -min_)
        out.append(new_ele)
    print(out)


if __name__ == '__main__':
    my_solution_32(inputs)