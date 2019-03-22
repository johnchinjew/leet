class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff = {}
        for i, x in enumerate(nums):
            if x in buff:
                return [buff[x], i]
            else:
                buff[target - x] = i
