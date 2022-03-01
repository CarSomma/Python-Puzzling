"""16. Write a Python program find the strings
in a given list containing a given substring. 
Go to the editor
Input:
[('ca',('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[('oe',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
Click me to see the sample solution
"""
from utils import print_my_solution

input_1 = [('ca',('cat', 'car', 'fear', 'center'))]
input_2 = [('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
input_3 = [('oe',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
inputs = [input_1,input_2,input_3]

@print_my_solution(inputs)
def my_solution_16(input_):
    sub_str = input_[0][0]
    words_tuple = input_[0][1]

    matched_words = []
    for word in words_tuple:
        if sub_str in word:
            matched_words.append(word)

    print(matched_words)

if __name__ == '__main__':
    my_solution_16(inputs)