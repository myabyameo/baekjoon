import sys
def fi(a):
    if a==0:
        return 0
    else:
        return int((((1+5**0.5)/2)**a-((1-5**0.5)/2)**a)/(5**0.5))
T = int(sys.stdin.readline())
for i in range(T):
    a=int(sys.stdin.readline())
    if a==0:
        print(1, 0)
    else:
        print(fi(a-1), fi(a))