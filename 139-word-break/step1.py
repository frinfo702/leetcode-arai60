class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # 動的計画法のメモのため
        dp[0] = True # len(s)が0なら必ず分割可能
        words = set(wordDict)
        max_word_length = max(len(word) for word in words)

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_word_length) , i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
