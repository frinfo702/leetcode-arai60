class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memorize result
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for start_i in range(len(s)):
            for end_i in range(start_i+1, len(s)):
                if s[start_i] and s[start_i:end_i] in wordDict:
                    dp[end_i] = True
                    break
        return dp[len(s)]