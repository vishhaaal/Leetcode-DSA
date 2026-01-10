class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []
        for num in nums1:
            seen[num] = seen.get(num,0) + 1

        for num in nums2:
            if num in seen and seen[num] > 0:
                result.append(num)
                seen[num] -= 1

        return result
        
