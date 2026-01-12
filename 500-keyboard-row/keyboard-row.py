class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = word.lower()
            char = set(w)

            if char.issubset(row1) or char.issubset(row2) or char.issubset(row3):
                result.append(word)

        return result

        