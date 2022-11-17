class Solution:
    #def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap