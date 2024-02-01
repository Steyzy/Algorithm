# this is the implementation of a min heap

from typing import List
from collections import defaultdict

# converts an arbitrary array into one that obeys heap property
def heapify(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        insert(res, num)
    return res


# insert a new element to the end of array, then bubble it up
def insert(array: List[int], num: int) -> None:
    array.append(num)
    i = len(array)-1
    while i>0:
        parent = array[(i-1)//2]
        if array[i]<parent:
            array[i], array[(i-1)//2] = array[(i-1)//2], array[i]
        i = (i-1)//2


# pop the top element, fill the gap with the last element of array, and bubble it down
def pop(array: List[int]) -> int:
    # bubble down the top element
    def pop_helper(n: int) -> None:
        i = 0
        while True:
            child1, child2 = 2*i+1, 2*i+2
            if child1>=n: break
            elif child2>=n:
                if array[child1]<array[i]:
                    array[i], array[child1] = array[child1], array[i]
                    i = child1
                else: break
            else:
                min_child = min(array[child1], array[child2])
                min_idx = child1 if min_child==array[child1] else child2
                if array[min_idx]<array[i]:
                    array[i], array[min_idx] = array[min_idx], array[i]
                    i = min_idx
                else: break
    
    array[0], array[-1] = array[-1], array[0]
    min_val = array.pop(-1)
    pop_helper(len(array))
    return min_val


# sort in ascending order
def heapsort(array: List[int]) -> List[int]:
    res = []
    for i in range(len(array)):
        res.append(pop(array))
    return res
    
    
# this is a test for heap
nums = [8,2,5,6,4,3,1,7]
my_heap = heapify(nums)
# print(my_heap)
print(heapsort(my_heap))