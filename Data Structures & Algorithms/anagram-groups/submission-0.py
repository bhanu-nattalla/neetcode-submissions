class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                # Map each lowercase character to an index from 0 to 25
                position = ord(char) - ord('a')
                count[position] += 1

            signature = tuple(count)

            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]

        return list(groups.values())