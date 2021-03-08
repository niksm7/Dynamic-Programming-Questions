def LCS(x, y, m, n):
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif y[i - 1] == x[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],L[i][j-1])

    return L[n][m]


x = "AGGTAB"
y = "GXTXAYB"
m = len(x)
n = len(y)

L = [[0 for i in range(m + 1)] for j in range(n + 1)]

a = LCS(x, y, m, n)
print(a)