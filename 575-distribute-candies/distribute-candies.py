class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)//2

        seen = {}
        for num in candyType:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        unique_types = len(seen)
        return min(unique_types, n)
