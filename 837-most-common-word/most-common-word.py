class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        seen = {}

        cleaned = ""
        for ch in paragraph:
            if ch.isalpha():
                cleaned += ch.lower()
            else:
                cleaned += " "
        
        words = cleaned.split()
        max_count = 0
        answer = ""

        for word in words:
            if word not in banned_set:
                seen[word] = seen.get(word,0) + 1
                if seen[word] > max_count:
                    max_count = seen[word]
                    answer = word
        return answer