class Solution:
    def isValid(self, s: str) -> bool:
        # ペアごとにインデックスは揃えておく
        open_brankets = ["(", "{", "["]
        close_brankets = [")", "}", "]"]
        branket_stack = []

        for char in s:
            if char in open_brankets:
                branket_stack.append(char)
            elif char in close_brankets:
                if not branket_stack:
                    return False
                if open_brankets.index(branket_stack[-1]) != close_brankets.index(char):
                    return False
                else:
                    branket_stack.pop()
                    continue

        if len(branket_stack) == 0:
            return True
        else:
            return False
