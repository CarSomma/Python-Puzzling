"""
Write a Python program to sort the numbers of a given list by the sum of their digits. Go to the editor
Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
Output:
[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Input: [23, 2, 9, 34, 8, 9, 10, 74] 
Output:
[10, 2, 23, 34, 8, 9, 9, 74]
"""

input1= [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
input2= [23, 2, 9, 34, 8, 9, 10, 74] 
inputs = [input1, input2]



def calculate_sum(number):
    sums = []
    if len(str(number)) ==1:
        sums.append(number)
    else:
        for char1, char2 in zip(str(number),str(number)[1:]):
            sum_ = int(char1) + int(char2)
            #print(sum_,char1, char2)
            sums.append(sum_)
    return sums


def my_solution_38(inputs_):
    for input_ in inputs_:
        print(f"Input: {input_}")
        print(f'Output:')
        print(sorted(input_,key=lambda x: calculate_sum(x), reverse=False))


if __name__ == "__main__":
    my_solution_38(inputs)
