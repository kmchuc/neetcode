class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        tracker = set()
        max_substring = 0
        for right in range(len(s)):
            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1
            tracker.add(s[right])
            max_substring = max(max_substring, right - left + 1)
        return max_substring