class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keep_set = set()

        for num in nums:
            if num in keep_set:
                return True
            else:
                keep_set.add(num)
        return False