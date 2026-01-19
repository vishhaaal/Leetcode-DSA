class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        seen = {}

        for card in deck:
            seen[card] = seen.get(card, 0) + 1

        counts = list(seen.values())
        min_count = min(counts)

        for x in range(2,min_count + 1):
            valid = True
            for count in counts:
                if count % x != 0:
                    valid = False
                    break
            if valid:
                return True
            
        return False