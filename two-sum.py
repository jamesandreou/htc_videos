class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # a + b = target
        # b = target - a
        bVals = {}
        for i in range(0, len(nums)):
            a = nums[i]
            b = target - a
            if a in bVals:
                return [bVals[a], i]
            else:
                bVals[b] = i