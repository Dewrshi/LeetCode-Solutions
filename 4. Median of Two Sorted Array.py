class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums1:
            nums2.append(i)
        nums2.sort()
        median = 0.00000
        n=len(nums2)-1
        a=int((n+1)/2)
        if(n%2!=0):
            median = (nums2[int(n/2)]+nums2[a])/2
            print(nums2[a])
            print(nums2[int(n/2)])
        else:
            median = nums2[a]
        return median
        
