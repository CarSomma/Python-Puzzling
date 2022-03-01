"""2. Write a Python program that accept 
a list of integers and check the length and the fifth element.
Return true if the length of the list is 8 and fifth element occurs thrice in the said list. Go to the editor
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
Click me to see the sample solution
"""
from utils import counter,print_my_solution

input_1 = [19, 19, 15, 5, 5, 5, 1, 2]
input_2 = [19, 15, 5, 7, 5, 5, 2]
input_3 = [11, 12, 14, 13, 14, 13, 15, 14]
input_4 = [19, 15, 11, 7, 5, 6, 2]

inputs = [input_1, input_2, input_3, input_4]


@print_my_solution(inputs)
def my_solution_2(input_list:list, len_list:int, pos_item:int, expected_count:int):
    
    if len(input_list) !=len_list:
        print(False)
    else:
        count_dict = counter(input_list)
        if count_dict[input_list[pos_item]] == expected_count:
            print(True)
        else:
            print(False)
            
if __name__ == "__main__":
    my_solution_2(inputs,len_list = 8,pos_item = 4, expected_count=3)