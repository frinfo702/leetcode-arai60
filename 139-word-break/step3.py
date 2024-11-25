class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_partition = len(s) + 1
        can_break = [False] * num_partition
        can_break[0] = True
        words = set(wordDict)
        max_word_length = max(len(word) for word in words)

        for end_i in range(1, len(s) + 1):
            for start_i in range(max(0, end_i - max_word_length), end_i):
                substring = s[start_i:end_i]
                if can_break[start_i] and substring in words:
                    can_break[end_i] = True
        
        return can_break[-1]
