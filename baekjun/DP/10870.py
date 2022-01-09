zero = [1,0,1]
one = [0,1,1]

def fibonacci(n):
    leng = len(zero)
    if n >= leng:
        for i in range(leng, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[n],one[n]))

N = int(input())

for _ in range(N):
    fibonacci(int(input()))
