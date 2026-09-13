from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, occurance in counter.items():
            heapq.heappush(heap, (occurance, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for occurance, num in heap]