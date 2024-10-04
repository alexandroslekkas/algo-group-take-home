# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    input.sort()
    print(input)
    previousNum = -1
    for num in input:
        print(num)
        if (num == previousNum):
            return num
        previousNum = num
    
list = [1,2,3,6,8,3,4]
print("Duplicate:", findDuplicate(list))

# This should be O(n) I believe because it will increase linearly in complex
# as the list size increases