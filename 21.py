from __future__ import print_function
import sys
#import numpy as np
#from numpy import median

def rotate(l, n):
    return l[-n:] + l[:-n]

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return int(sorted(lst)[n//2])*2.0
    else:
#            return int(sum(sorted(lst)[(n//2-1):(n//2+1)])//2.0)
            return int(lst[(n//2-1)]) + int(lst[(n//2-1)])+1

my_e = 0
r = ()
#m = 0

q = sys.stdin.readline().strip().split(' ')
f = sys.stdin.readline().strip().split(' ')

#np.array(q).astype(np.int)
#np.array(f).astype(np.int)

num0 = int(q[1])
#num1 = num0 + 1
#print (num1)
num2 = int(q[0])-num0

#print (f[0:num1-1])

for k in range(int(num2)):
    r = f[0:num0]
#    np.array(r).astype(np.float)

    m = int(median(r))
    print('Med : ',m)
    print('Dyn : ',f[num0])
    print(r)
    
    if (int(median(r)) <= int(f[num0])): 
        my_e = my_e + 1
        print('Rez : ', my_e)

    f = rotate(f, -1)
        
print(my_e)

