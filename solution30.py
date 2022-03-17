"""30. Write a Python program to find
the list of strings that has fewer
total characters (including repetitions). Go to the editor
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
Click me to see the sample solution

"""
from utils import print_my_solution

input_1 = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
input_2 = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
inputs = [input_1, input_2]

@print_my_solution(inputs)
def my_solution_30(input_):
    shifted_input = input_[1:]

    for first, second in zip(input_, shifted_input):
        strings1 = "".join(first).replace(" ","")
        strings2 = "".join(second).replace(" ","")
        if len(strings1) < len(strings2):
            print(first)
        else:
            print(second)


if __name__ == '__main__':
    my_solution_30(inputs)
