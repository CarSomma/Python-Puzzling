"""Here some useful function for solving the tasks"""

def counter(input_list):
    """It counts the occurance of list items.
       It return a mapping between list item and occurance count
    """
    count_dict = {}
    for number in input_list:
        if number not in count_dict.keys():
            count_dict[number] = 1
        else:
            count_dict[number] += 1
    return count_dict


def find_uniques(input_):
    """It returns unique values list from an input list """
    uniques = []
    for item in input_:
        if input_.count(item) >= 1 and item not in uniques:
            uniques.append(item)
    return uniques



# https://parseltongue.co.in/how-to-write-a-decorator-in-pythonfunction-based/
def print_my_solution(inputs):
    def decorate(func):
        def inner(*args, **kwargs):
            for input_ in inputs:
                print(f"Input:\n{input_}")
                print(f"Output:")
                func(input_,**kwargs)
        return inner
    return decorate

@print_my_solution([3,4,5])
def who(list_1= [3,4,5]):                                                                                                  
    print(list_1)                                                                                          
                                                                                                            
def print_my_solution_2(klist_,input_):
    def decorate(func):
        def inner(*args, **kwargs):
            for k in klist_:
                print(f"Input:\n{input_}")
                print(f"Output:")
                func(input_,k, **kwargs)
        return inner
    return decorate                                                    
                                                                                                            
if __name__ == "__main__":
    who([3,4,5])                                                                                
                                                                                               

