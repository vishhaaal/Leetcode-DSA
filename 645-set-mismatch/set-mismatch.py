class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = {}
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            seen[num] = seen.get(num,0) + 1

        for num in seen:
            if seen[num] > 1:
                result.append(num)

        total = n * (n + 1)//2
        answer = total - sum(set(nums))
        result.append(answer)
        return result
        
        