from __future__ import print_function
import sys
n1 =  sys.stdin.readline().strip().replace(',','').split(' ')

def my_sorted(a):
    n = 1
    while n < len(a):
         for i in range(len(a)-n):
              if int(a[i]) > int(a[i+1]):
                   a[i],a[i+1] = a[i+1],a[i]
         n += 1
    return a

n1 = my_sorted(n1)

def find_arith(aplist):
   idiff=[]
   flag=0
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
         print ('>',i)
# 963, 1405, 1301, 950, 1028, 391, -12, 326, 222, 1249, 1067, 170, 937, 911, 664, 651, 300, 1327, 14, 1171, 105, 274, 417, 1340, 547, 378, 53, 807, 1158, 638, 1197, 248, 1379, 586, 1054, 794, 352, 404, 625, 209, 1106, 235, 1132, 1041, 456, 469, 573, 183, 924, 1457, 1353, 1002, 755, 872, 118, 1314, 716, 1093, 1431, 729, 898, 885, 677, 430, 1262, 1366, 1015, 742, 1236, 495, 534, 131, 313, 1184, 261, 976, 1418, 40, 1288, 1496, 703, 27, 820, 1275, 287, 79, 859, 1223, 157, 781, 1080, 144, 599, 1392, 989, 339, 768, 66, 1483, 1145, 508, 521, 1444, 1470, 1119, 92, 482, 365, 1210, 443, 612, 833, 1, 560, 846, 690 
         
find_arith(n1)
