class Solution:
    def isValid(self, s: str) -> bool:
        # ペアごとにインデックスは揃えておく
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        bracket_stack = []

        for char in s:
            if char in open_brackets:
                bracket_stack.append(char)
            elif char in close_brackets:
                if not bracket_stack:
                    return False
                if open_brackets.index(bracket_stack[-1]) != close_brackets.index(char):
                    return False
                else:
                    bracket_stack.pop()
                    continue

        if len(bracket_stack) == 0:
            return True
        else:
            return False
