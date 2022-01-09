N = int(input())

def score(n):
    if n >= 90:
        return print('A')
    elif n >= 80:
        return print('B')
    elif n >= 70:
        return print('C')
    elif n >= 60:
        return print('D')
    else:
        return print('F')

score(N)