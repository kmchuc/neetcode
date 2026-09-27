class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1, pointer2 = 0, len(numbers) - 1

        while pointer1 < pointer2:
            curr_sum = numbers[pointer1] + numbers[pointer2]
            if curr_sum > target:
                pointer2 -= 1
            elif curr_sum < target:
                pointer1 += 1
            else:
                return [pointer1 + 1, pointer2 + 1]
        return 