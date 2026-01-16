class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}
        for i,num in enumerate(nums):
            count[num] = count.get(num,0) + 1

            if num not in first:
                first[num] = i
            last[num] = i

        min_length = len(nums)
        degree = max(count.values())

        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)
        return min_length
