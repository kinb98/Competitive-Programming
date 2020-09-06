class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0
        while ind < len(nums):
            if(nums[ind] == target or nums[ind] > target):
                return ind
            ind += 1 
        return ind