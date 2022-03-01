"""Write a Python program find a list of integers
 with exactly two occurrences of nineteen and at 
 least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True"""
#import sys
from utils import counter, print_my_solution
input_1 = [19, 19, 15, 5, 3, 5, 5, 2]
input_2 = [19, 15, 15, 5, 3, 3, 5, 2]
input_3 = [19, 19, 5, 5, 5, 5, 5]
inputs = [input_1, input_2, input_3]
#def to_int(*args):
 #   return [int(x) for x in args]
@print_my_solution(inputs)
def my_solution_1(input_list:list,num1:int, num2:int, expected_count1:int, expected_count2:int):
    
    count_dict = counter(input_list)
    if count_dict[num1]== expected_count1 and count_dict[num2] >= expected_count2:
        print(True)
    else:
        print(False)

# def main():
#     for input_ in inputs:
#        print(f"Input:\n{input_}")
#        print(f"Output:")
#        my_solution_1(input_,19,5,2,3)



if __name__ == "__main__" :
    #print(sys.argv[1:])
   # into_int(*sys.argv[1:])
   my_solution_1(inputs, num1=19, num2=5, expected_count1=2,expected_count2=3)
