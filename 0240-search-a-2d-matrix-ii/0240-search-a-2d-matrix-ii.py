class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1
        n=len(matrix[0])
        i=m
        j=0
        while i>=0 and j<n:
            if target<matrix[i][j]:
                i-=1
                continue
            elif target>matrix[i][j]:
                j+=1
                continue
            else:
                return True
        """def binary_search(arr, low, high, x):
            if high >= low:
                mid = (high + low) // 2
                # If element is present at the middle itself
                if arr[mid] == x:
                    return True
                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)
                else:
                    return binary_search(arr, mid + 1, high, x)
            else:
                # Element is not present in the array
                return False
        for i in matrix:
            if binary_search(i,0,len(i)-1,target):
                print(i)
                return True
            else:
                continue
        return False
            """
                
        