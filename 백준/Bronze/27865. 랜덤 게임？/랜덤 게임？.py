import sys
n=int(input())
while True:
    sys.stdout.write('? 1\n')
    sys.stdout.flush()
    i=sys.stdin.readline().strip()
    if i=='Y':
        sys.stdout.write('! 1\n')
        sys.stdout.flush()
        break