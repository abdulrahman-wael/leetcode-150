class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I didn't solve this problem (because I was not patient to fix my solution)


        # sample solution 1 (RELATED ALGO: set data structure )
        # nums[:] = sorted(set(nums))

        # sample solution 2: 
        # if not nums:
        #     return 0
        # idx = 1
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[idx] = nums[i]
        #         idx+=1
        # del nums[idx+1:]
        # return idx
            
        