def LCS(x, y, m, n):
    result = 0 #we need to create a variable result beacause the longest substring can exist anywhere and not just the ending
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif y[i - 1] == x[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                result = max(result, L[i][j]) # we take the max so that we can return the longest substring
            else:
                L[i][j] = 0

    return result

# with this input try removing the line 2 and 9 and return L[m][n] you will get 1 as the answer because it won't consider AB as longest but only B as the longest as it is at the end.

x = "aacabdkacaa"
y = "bkaac"
# Longest Common Substring will be "aac" and its length is 3
m = len(x)
n = len(y)

L = [[0 for i in range(m + 1)] for j in range(n + 1)]

a = LCS(x, y, m, n)
print(a) 