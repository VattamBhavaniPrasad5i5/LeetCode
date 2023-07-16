class Solution:
    def largestVariance(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        permutations = itertools.permutations(chars, 2)
        count = 0
        for a, b in permutations:
            count = max(self.kadene(a, b, s, chars), count)
        return count

    def kadene(self, a, b, s, chars):
        count = 0
        max_local = 0
        is_a = False
        is_b = False

        val_a = chars[a]
        val_b = chars[b]
        for c in s:			
            if c != a and c != b:
                continue

            if max_local < 0 and val_a != 0 and val_b != 0:
                max_local = 0
                is_a = False
                is_b = False

            if c == a:
                max_local += 1
                val_a -= 1
                is_a = True
						
            if c == b:
                max_local -= 1
                val_b -=1
                is_b = True
            
            if is_a and is_b:
                count = max(count, max_local)
        return count