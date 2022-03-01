"""15. Write a Python program find the 
longest string of a given list of strings. 
Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
Click me to see the sample solution
"""
from numpy import sort,argsort
from utils import print_my_solution


input_1 = ['cat', 'car', 'fear', 'center']
input_2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '','scoobidubidu']
inputs = [input_1, input_2]

# fast solution
@print_my_solution(inputs)
def my_fast_solution_15(input_):
    print(sorted(input_, key= lambda x: len(x), reverse=True)[0])

@print_my_solution(inputs)
def my_solution_15(input_):
    word_out = []
    max_length = 0
    for word in input_:
        if len(word)>= max_length:
            max_length = len(word)
            word_out.insert(0,word)
    print(word_out[0])


@print_my_solution(inputs)
def my_solution_15_2(input_):
    words_out = []
    word_length_list = []

    for word in input_:
        word_length_list.append(len(word))

    sorted_length_index = argsort(word_length_list)[-1::-1]
    for idx, word in enumerate(input_):
        words_out.insert(idx,input_[sorted_length_index[idx]])

    print(words_out)
    print(words_out[0])
# length_max = 0  
# for word in input_2:
#     word_length_dict[word]= len(word)
#     if len(word) >= length_max:
#         words_out.insert(0,word)
#         length_max = len(word)
#     else:
#         for index, out_word in enumerate(words_out):
#             if len(word) > word_length_dict[out_word]:
#                 words_out.insert(index,word)
#             else:
#                 words_out.append(word)

    
#print(words_out)
if __name__ == '__main__':
    my_solution_15_2(inputs)