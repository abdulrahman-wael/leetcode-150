class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, dups = 1,0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
                dups = 0
            elif dups < 1:
                nums[idx] = nums[i]
                idx += 1 
                dups += 1
        del nums[idx:]


        # another solution (not MINE)
        # change the duplicate into INT_MAX and sort

        # elegant solution (modified from another solution: not MINE)
        # i = 2

        # for j in range(2, len(nums)):
        #     if nums[j] != nums[i - 2]:
        #         nums[i] = nums[j]
        #         i += 1      
        # del nums[i:]

        