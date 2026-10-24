# RELATED ALGO: Dynamic programming
class Solution(object):
    def canJump(self, nums):
        # This is OPENCODE LLM solution: inversion + induction.
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        