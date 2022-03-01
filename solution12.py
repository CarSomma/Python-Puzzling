"""12. Write a Python program to check
 whether the given strings are palindromes
  or not. Return True, False. Go to the editor
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
Click me to see the sample solution
"""


input_ = ['palindrome', 'madamimadam', '', 'foo', 'eyes']



def my_solution(input_):

    output = []
    for word in input_:
        if word == word[-1::-1]:
            output.append(True)
        else:
            output.append(False)
    print('Input:')
    print(f'{input_}')
    print('Output:')
    print(f'{output}')
    

if __name__ == "__main__":
    my_solution(input_)