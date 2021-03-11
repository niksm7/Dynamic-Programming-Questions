# Most of the code is same as PrintLCS and the only changes are after line 23 (minor changes)

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

LCS(x, y, m, n)



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

            #Here as we are calculating SCS so as we move to left we add to the string j-1 value which we are leaving behind
            LongCS += x[j-1]

            j -= 1
        else:

            #As we move to top we add to the string i-1 value which we are leaving behind
            LongCS += y[i-1]

            i -= 1 #If the number above is bigger then we move one step up i.e. i--

# Now in the while condition above we are checking "or" condition for i and j becoming 0 but there must be a scenario where either of them is not 0 but as we are finding SCS we need to add those left in the x or y string to the LongCS string.

while j > 0:
    LongCS += x[j-1]
    j -= 1
while i > 0:
    LongCS += y[i-1]
    i -= 1

print(LongCS[::-1])