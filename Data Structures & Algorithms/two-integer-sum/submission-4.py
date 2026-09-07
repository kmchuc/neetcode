class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_tracker = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_tracker:
                return [diff_tracker[diff], i]
            else:
                diff_tracker[nums[i]] = i
            
        return []