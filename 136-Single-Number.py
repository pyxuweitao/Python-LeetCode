__author__ = 'xuweitao'
#runtime = 82ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums     = sorted(  nums, cmp )
        for i in range(0,len(nums[:-1]),2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]