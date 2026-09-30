class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = len(nums) - k % len(nums)
        nums[:] = nums[m:] + nums[:m]

        # another Solution
        # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        
        