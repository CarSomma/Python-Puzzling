"""8. Write a Python program to split
a string of words separated by commas 
and spaces into two lists, words and separators.
Go to the editor
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
Click me to see the sample solution
"""
import re
from utils import print_my_solution

input_1 = 'W3resource Python, Exercises.'
input_2 = "The dance, held in the school gym, ended at midnight."
input_3 = "The colors in my studyroom are blue, green, and yellow."
inputs = [input_1, input_2, input_3]
#print(input_1.split(" "))
# for ch in input_1:
#     if ch.
@print_my_solution(inputs)
def my_solution_8(input_):
    string = input_
    char_list = re.split(r"[, ]+",string)
    commas_space_list = re.findall(r"[\s,]+",string)
    print([char_list, commas_space_list])

if __name__ == '__main__':
    my_solution_8(inputs)