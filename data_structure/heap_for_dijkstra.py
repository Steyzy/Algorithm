# this is the implementation of a min heap tailored for Dijkstra's algorithm implementation

from typing import List
from collections import defaultdict

class Element:
    def __init__(self, score: int, node: int):
        self.score = score
        self.node = node


# converts an arbitrary array into one that obeys heap property
def heapify(array: List[Element]) -> List[Element]:
    res = []
    for ele in array:
        insert(res, dict(), ele)
    return res


def bubble_up(heap: List[Element], index_map: dict[int, int], i: int):
    while i>0:
        parent = (i-1)//2
        if heap[i].score<heap[parent].score:
            # swap index
            index_map[heap[parent].node] = i
            index_map[heap[i].node] = parent
            # swap heap elements
            heap[i], heap[parent] = heap[parent], heap[i]
        else: break
        i = parent


def bubble_down(heap: List[Element], index_map: dict[int, int], i: int):
    n = len(heap)
    while True:
        child1, child2 = 2*i+1, 2*i+2
        # leaf node
        if child1>=n: break
        # left child non-null
        elif child2>=n:
            if heap[child1].score<heap[i].score:
                # swap index
                index_map[heap[child1].node] = i
                index_map[heap[i].node] = child1
                # swap heap elements
                heap[i], heap[child1] = heap[child1], heap[i]
                i = child1
            else: break
        # both children non-null
        else:
            min_child = min(heap[child1].score, heap[child2].score)
            min_idx = child1 if min_child==heap[child1].score else child2
            if heap[min_idx].score<heap[i].score:
                # swap index
                index_map[heap[min_idx].node] = i
                index_map[heap[i].node] = min_idx
                # swap heap elements
                heap[i], heap[min_idx] = heap[min_idx], heap[i]
                i = min_idx
            else: break


# insert a new element to the end of array, then bubble it up
def insert(heap: List[Element], index_map: dict[int, int], ele: Element) -> None:
    heap.append(ele)
    i = len(heap)-1
    index_map[ele.node] = i   
    bubble_up(heap, index_map, i)


# pop the top element, fill the gap with the last element of array, and bubble it down
def pop(heap: List[Element], index_map: dict[int, int]) -> Element:
    heap[0], heap[-1] = heap[-1], heap[0]
    min_ele = heap.pop(-1)
    del index_map[min_ele.node]
    # print([[vertex.score, vertex.node] for vertex in heap])
    index_map[heap[0].node] = 0
    bubble_down(heap, index_map, 0)
    return min_ele


def build_map(heap: List[Element]) -> dict[int, int]:
    res = dict()
    for i in range(len(heap)):
        node = heap[i].node
        res[node] = i
    return res


# decrease the value of a certain key (corresponding to a certain index in heap), then bubble it up
def decrease_key(heap: List[Element], index_map: dict[int, int], node: int, score: int):
    i = index_map[node]
    heap[i].score = score   #update the score
    bubble_up(heap, index_map, i)


# vertices = [Element(3,1), Element(4,2), Element(1,3), Element(5,4), Element(2,5)]
# # print(build_map(heapify(vertices)))
# heap = []
# index_map = dict()
# for vertex in vertices:
#     insert(heap, index_map, vertex)
#     print(index_map)
#     # print([vertex.score for vertex in heap])

# decrease_key(heap, index_map, 4, 1)
# print([vertex.score for vertex in heap])
# for i in range(len(heap)):
#     print(pop(heap).score)