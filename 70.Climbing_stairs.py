def climb_stairs(n):
    if (n)==1:
        return 1
    if (n)==2:
        return 2
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]

b=int(input("Enter the number of stairs: "))

while True:
    if b<1:
        print("Number of stairs cannot be less than 1.")
        break
    if b>45:
        print("number of stairs cannot be more than 45.")
        break
    else:
        print(climb_stairs(b))
        break



