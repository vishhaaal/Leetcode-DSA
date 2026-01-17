class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        runes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformation = set()
        for word in words:
            code = ""
            for ch in word:
                code += runes[ord(ch) - ord('a')]
            transformation.add(code)
        return len(transformation)
