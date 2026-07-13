class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(2, 10):
            for start in range(1, 10 - length + 1):
                num = int("".join(str(d) for d in range(start, start + length)))
                if low <= num <= high:
                    result.append(num)
        return result