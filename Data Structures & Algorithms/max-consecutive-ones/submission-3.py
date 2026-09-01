class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if len(nums) == 1 and nums[0] != 1:
            return 0
        

        tracker = 0
        max_counter = 0

        for i in nums:
            if i == 1:
                tracker += 1
            else:
                max_counter = max(max_counter, tracker)
                tracker = 0
        
        return max(max_counter, tracker)