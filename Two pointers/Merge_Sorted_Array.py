class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return
        if m ==0:
            nums1[:] = nums2[:]
        A = m-1
        B = n-1
        C = n+m-1
        while A >= 0 and B >= 0:
            if nums2[B] >= nums1[A]:
                nums1[C] = nums2[B]
                # A is the same
                B -=1
                C -=1
            else:
                nums1[C] = nums1[A]
                A -=1
                # B is the same
                C -=1


        # an edge case that I didn't recognize: what if nums1 contains 4,5,6,0,0,0 and nums2 1,2,3
        #   nums2 now have leftovers
        #   nums1 cannot have leftovers in this example or any other.
        while B >= 0:
            nums1[C] = nums2[B]
            B -= 1
            C -= 1


                
