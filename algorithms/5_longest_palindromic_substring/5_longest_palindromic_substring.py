class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        T = [[False] * n] * n
        for i in range(0, n):
            T[i][i] = True
        res = s[0]
        for l in range(1, n):
            for i in range(0, n - l):
                j = i + l
                T[i][j] = (s[i] == s[j]) and ((l == 1) or ((l > 1) and T[i+1][j-1]))
                if (T[i][j] and l > len(res)):
                    res = s[i : j + 1]
        return(res)
