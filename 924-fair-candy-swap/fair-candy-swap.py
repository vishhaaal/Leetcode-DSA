class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumA - sumB)//2
        bobset = set(bobSizes)

        for x in aliceSizes:
            y = x - diff
            if y in bobset:
                return [x,y]
        