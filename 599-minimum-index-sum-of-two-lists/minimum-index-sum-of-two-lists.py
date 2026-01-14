class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        seen = {}

        for i, word in enumerate(list1):
            seen[word] = i

        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in seen:
                curr_sum = j + seen[word]
                if min_sum > curr_sum:
                    min_sum = curr_sum
                    result = [word]
                elif min_sum == curr_sum:
                    result.append(word)
        return result