class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        ---Hashmap Method---
        seen = {}
        target = len(nums)/2

        for num in nums:
            seen[num] = seen.get(num,0) + 1
            if seen[num] > target:
                return num 
        """
        count = 0
        number = None

        for num in nums:
            if count == 0:
                number = num
            count += 1 if num == number else -1
        
        return number