import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()

il = int(b[2])
sip = int(b[1])
baek = int(b[0])

print(a*il)
print(a*sip)
print(a*baek)
print(a*il + 10*a*sip + 100*a*baek)