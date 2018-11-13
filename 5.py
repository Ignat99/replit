#from __future__ import print_function
import sys

def my_sorted(a):
    n = 1
    while n < len(a):
         for i in range(len(a)-n):
              if int(a[i]) > int(a[i+1]):
                   a[i],a[i+1] = a[i+1],a[i]
         n += 1
    return a

def find_missing(aplist):
   idiff=[]
   flag=0
   aplist = my_sorted(aplist)
   for j in range(0, len(aplist)-1):
      diff1 = int(aplist[j+1]) - int(aplist[j])
      if diff1 < 0:
         flag=1
      idiff.append(abs(diff1))
   if flag==1:
     final_diff=-1*min(idiff)
   else:
     final_diff=min(idiff)

   for i in range(int(aplist[0]),int(aplist[len(aplist)-1])+1,final_diff):
      if str(i) not in aplist:
         return (i)

n1 =  sys.stdin.readline().replace(',','').strip().split(' ')

print (find_missing(n1))
