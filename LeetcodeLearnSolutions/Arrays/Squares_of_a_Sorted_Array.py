class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        l = 0
        r = n-1
        for i in range(n-1,-1,-1):
            if abs(nums[l]) < abs(nums[r]):
                sq=nums[r]
                r-=1
            else:
                sq=nums[l]
                l+=1
            result[i]=sq*sq
        return result
