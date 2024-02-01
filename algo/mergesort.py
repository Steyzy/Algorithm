class Solution:
    #mergesort implementation
    def mergeArray(self, a: List[int], b: List[int]) -> List[int]:
        i, j = 0, 0
        la, lb = len(a), len(b)
        res = []
        while (i<la and j<lb):
            if (a[i]<=b[j]): 
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        res.extend(a[i:])
        res.extend(b[j:])
        return res
        
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==0 or n==1: return nums
        sorted1 = self.sortArray(nums[:n//2])
        sorted2 = self.sortArray(nums[n//2:])
        return self.mergeArray(sorted1, sorted2)
        