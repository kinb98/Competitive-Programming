class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far,mx = 0,0
        if max(nums) < 0:
            return max(nums)
        else:
            for i in nums:
                max_so_far += i
                if max_so_far < 0:
                    max_so_far = 0
                mx = max(max_so_far,mx)
        return mx