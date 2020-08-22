# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Write a function:
#class Solution { public int solution(int[] A); }
#that, given an array A of N integers, returns the
# smallest positive integer (greater than 0) that does not occur in A.
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 3], the function should return 4.
#Given A = [−1, −3], the function should return 1.
#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].

import random

numList = []

#maybe we can use sys.maxsize -
# funct to create max n min int value
min_index = 0
max_index = 10

result = 1;

range_of_array = int(input("Please enter the array size: "))

for i in range(range_of_array):
    numList.append(random.randrange(min_index, max_index))

for i in numList:
    print(i)

for i in range(range_of_array):
    if result in numList:
        result += 1

print(result)
