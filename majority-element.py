class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I was NOT PATIENT enough to solve this by myself in 15 min.

        # a solution
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]


        # another solution using dict (using another type of dict will be more efficient by the way)
        # n = len(nums)
        # s = dict()

        # for num in nums:
        #     if not s.get(num):
        #         s.update({num: 1})
        #     else:
        #         s[num] +=1
        #     if s[num] > n//2:
        #         return num
        
        # the best one: MOORE voting algorithm
        condidate, count = 0,0
        for num in nums:
            if count == 0:
                condidate = num

            if condidate == num:
                count += 1
            else:
                count -= 1
        return condidate