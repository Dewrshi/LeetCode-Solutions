class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        start = 0
        end=0
        letters = set()
        while end < len(s):
            while end < len(s) and s[end] not in letters:
                letters.add(s[end])
                end += 1 
            curr_len = len(letters)
            if curr_len > max_len:
                max_len = curr_len
            if end < len(s) and s[end] in letters:
                while s[start] != s[end]:
                    letters.remove(s[start])
                    start += 1
                letters.remove(s[start])
                start += 1
        return max_len
                
            
