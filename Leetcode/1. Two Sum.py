class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        flag = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
                    flag = 1
                    break
                if flag == 1:
                    break
        return l