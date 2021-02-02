class Solution:
    def palindromicPartition(self, s: str) -> int:
        n = len(s)
        T = [[0] * n for i in range(n)]
        for i in range(0, n):
            T[i][i] = 1
        for l in range(1, n):
            for i in range(0, n - l):
                j = i + l
                if (l <= 1):
                    if (s[i] == s[j]):
                        T[i][j] = 1
                    else:
                        T[i][j] = l + 1
                else:
                    if (s[i] == s[j] and T[i + 1][j - 1] == 1):
                        T[i][j] = 1
                    else:
                        T[i][j] = n
                        for k in range(i, j):
                            T[i][j] = min(T[i][j], T[i][k] + T[k + 1][j])

        return(T[0][n-1])
                
