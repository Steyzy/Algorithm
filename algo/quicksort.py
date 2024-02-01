class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(array, i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        def selectPivot(array, lo, hi):
            length = hi-lo+1
            if length in [0, 1, 2]: return
            b, m, e = lo, (length//2), hi
            median = sorted([array[b], array[m], array[e]])[1]
            if median==array[m]:
                swap(array, b, m)
            elif median==array[e]:
                swap(array, b, e)

        def partition(array, lo, hi):
            if lo==hi: return lo
            selectPivot(array, lo, hi)
            pivot = array[lo]
            leftwall = lo
            pivot_index = lo
            for i in range(lo+1, hi+1):
                if array[i]<pivot:
                    if array[leftwall]==pivot:
                        pivot_index = i
                    swap(array, i, leftwall)
                    leftwall+=1
            swap(array, pivot_index, leftwall)
            return leftwall

        def quickSort(array, lo, hi):
            if lo<hi:
                pivot = partition(array, lo, hi)
                quickSort(array, lo, pivot)
                quickSort(array, pivot+1, hi)
            return array

        return quickSort(nums, 0, len(nums)-1)