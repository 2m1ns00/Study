def solution(m, n, puddles):
    
    test = [[0]*(m+1) for i in range(n+1)]
    test[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                test[i][j] = 0
            else:
                test[i][j] = (test[i-1][j]+test[i][j-1]) % 1000000007


    return test[n][m]



print(solution(4,3,[[2,2]]))

