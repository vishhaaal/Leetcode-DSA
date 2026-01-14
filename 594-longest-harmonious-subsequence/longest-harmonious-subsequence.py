class Solution:
    def findLHS(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        longest = 0
        for num in seen:
            if num + 1 in seen:
                longest = max(longest, seen[num] + seen[num + 1])
        
        return longest