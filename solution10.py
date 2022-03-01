"""10. Given a string consisting of whitespace
and groups of matched parentheses (same number "(" and ")"), 
write a Python program to split it into groups
of perfectly matched parentheses without any whitespace. Go to the editor
Input: 
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input: 
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
Click me to see the sample solution
"""
from utils import print_my_solution
input_1 = "( ()) ((()()())) (()) ()"
input_2 = "() (( ( )() ( )) ) ( ())"
inputs = [input_1, input_2]

@print_my_solution(inputs)
def my_solution_10(input_):
    set_string_list = []
    set_string = ""
    for ch in input_.replace(" ",""):
        set_string += ch
        if set_string.count("(") == set_string.count(")"):
            set_string_list.append(set_string)
            set_string = ""
    print(set_string_list ) 


if __name__ == "__main__":
    my_solution_10(inputs)

