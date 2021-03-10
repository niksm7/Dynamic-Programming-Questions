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


x = "acbcf"
y = "abcdaf"
m = len(x)
n = len(y)

L = [[0 for i in range(m + 1)] for j in range(n + 1)]

LCS(x, y, m, n)

########## Changes are from here only ##############

i = n
j = m
LongCS = ""
while (i > 0 and j > 0): #This while loop will run untill we reach the first row or first column

    #Here we are checking if the character at x and y index are same and if so we add that character to the out LongCS string and also decrement the i and j value as we have to move diagonally.
    if y[i-1] == x[j-1]:
        LongCS += y[i-1]
        i -=1
        j-=1
    else:
        # If the characters are not same then we check the if the number above is greater or the one beside and move accordingly

        if L[i][j-1] > L[i-1][j]: #If the number besides is bigger then we move one step left that is j--
            j -= 1
        else:
            i -= 1 #If the number above is bigger then we move one step up i.e. i--
print(LongCS[::-1])
