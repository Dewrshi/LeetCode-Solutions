class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #brute force will cause error due to time complexity
     #   for i in range(len(nums)):
      #      for j in range(i+1,len(nums)):
       #         if nums[i] + nums[j] == target:
        #            return [i,j]
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx


