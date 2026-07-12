class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finarr = []
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                finarr.append(nums1[i])
                i += 1
            else:
                finarr.append(nums2[j])
                j += 1
        while i < n:
            finarr.append(nums1[i])
            i += 1
        while j < m:
            finarr.append(nums2[j])
            j += 1
        
        n = len(finarr)
        if n % 2 == 1:
            return finarr[n // 2]
        else:
            return (finarr[n // 2 - 1] + finarr[n // 2]) / 2