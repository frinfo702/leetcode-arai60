class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_partition = len(s) + 1 # sの各文字間の仕切りの数
        can_break = [False] * num_partition # 仕切りの最後で分割可能(True)なら最終的に分割可能
        can_break[0] = True # 仕切りの先頭は任意の文字列で分割可能
        words = set(wordDict)        
        max_word_length = max(len(word) for word in words)

        for end_i in range(1, len(s) + 1):
            for start_i in range(max(0, end_i - max_word_length),end_i):
                substring = s[start_i:end_i]
                # 新たな部分文字列が見つかり、その直前の仕切りで分割可能
                if can_break[start_i] and substring in wordDict:
                    can_break[end_i] = True
                    break

        return can_break[-1]
