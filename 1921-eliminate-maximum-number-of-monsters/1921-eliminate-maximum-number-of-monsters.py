class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        return next((t for t, arrival in enumerate(sorted(d/s for d, s in zip(dist, speed))) if arrival <= t), len(dist))
