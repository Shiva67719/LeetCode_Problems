class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_str = ""

            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(int(digit) for digit in group)

                next_str += str(total)

            s = next_str

        return s