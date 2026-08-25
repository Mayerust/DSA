class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = sum(
            int(c) for c in num[:half] if c != '?'
        )

        right_sum = sum(
            int(c) for c in num[half:] if c != '?'
        )

        left_q = num[:half].count('?')
        right_q = num[half:].count('?')

        # Odd number of '?' means Alice gets the final move
        if (left_q + right_q) % 2 == 1:
            return True

        # Bob can win only if the difference can be exactly balanced
        return left_sum - right_sum != 9 * (right_q - left_q) // 2