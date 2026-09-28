class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val > 50:
            return
        a = len(nums) -1
        b = a
        k = 0
        while a >= 0:
            if nums[a] == val:
                nums[a] = nums[b]
                a -=1
                b -=1
            else:
                a -=1
                k +=1
        del nums[k:]