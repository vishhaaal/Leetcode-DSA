class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        seen = {}
        result = []

        for num in arr1:
            seen[num] = seen.get(num, 0) + 1 
        
        for num in arr2:
            result.extend([num] * seen[num])
            del seen[num]

        for num in sorted(seen):
            result.extend([num] * seen[num])

        return result