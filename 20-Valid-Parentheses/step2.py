class Solution:
    def isValid(self, s: str) -> bool:
        # ペアごとにインデックスは揃えておく
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        brackets_stack = []

        for char in s:
            if char in open_brackets:
                brackets_stack.append(char)
            elif char in close_brackets:
                if not brackets_stack:
                    return False
                if open_brackets.index(brackets_stack[-1]) != close_brackets.index(
                    char
                ):
                    return False
                else:
                    brackets_stack.pop()
                    continue

        if len(brackets_stack) == 0:
            return True
        else:
            return False
