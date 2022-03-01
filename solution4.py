"""
4. We are making n stone piles! The first pile has n stones.
If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile. Go to the editor
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
Input: 20
Output:
[20, 22, 24, 26, 28, 30, 33, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
Click me to see the sample solution
"""
from utils import print_my_solution


input_1 = 2
input_2 = 10
input_3 = 3
input_4 = 17
input_5 = 20



inputs = [input_1, input_2, input_3, input_4, input_5]

@print_my_solution(inputs)
def my_solution_4(n_piles):

    ini_n_stones = n_piles
    output_piles = []

    for stone in range(ini_n_stones, 3*ini_n_stones,2):
        output_piles.append(stone)
    print(output_piles)


if __name__ == "__main__":
    my_solution_4(inputs)
