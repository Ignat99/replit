from __future__ import print_function
import sys

def rotate(l, n):
    return l[-n:] + l[:-n]

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return int((int(lst[(n//2-1)]) + int(lst[(n//2-1)]))/2.0)

my_e = 0
r = ()
r1 = 0

q = sys.stdin.readline().strip().split(' ')
f = sys.stdin.readline().strip().split(' ')

num0 = int(q[1])
num2 = int(q[0])-num0

for k in range(int(num2)+1):
    r = f[0:num0]
    print(r)
    r1 = int(f[num0])
    print(r1)
    print(int(median(r))*2)
    if (int(median(r))*2 >= r1): 
        my_e += 1
        print (my_e)

    f = rotate(f, -1)
        
print(my_e)

