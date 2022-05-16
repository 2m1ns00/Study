def solution(money):
    h = [0 for _ in range(len(money))]
    dp = [0 for _ in range(len(money))]
    h[-1] = money[1]
    h[-2] = money[0]
    h[:-2] = money[:]
    dp[0] = h[0]
    dp[1] = h[1]
    dp[2] = max(h[2], dp[0]+h[2])
    dp[3] = max(dp[0]+h[3], dp[1]+h[3])
    for i in range(4, len(money)):
        dp[i]= max(dp[i-3] + h[i]+h[i-2],dp[i-3] + h[i]+h[i-3])


    return
solution([1,2,3,4,5,6])