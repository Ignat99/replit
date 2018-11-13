# replit
Some test of Python


Condición
Recorrer los 100 primeros números naturales. Si un numero es multiplo de 3 imprime Fizz. Si es múltiplo de 5 imprime Buzz. Si es múltiplo de los dos imprime FizzBuzz.
Expected Output

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

HackerLand National Bank has a simple policy for warning clients about possible  fraudulent account activity. If the amount spent by a client on a  particular day is greater than or equal to 2x the client's median spending for the last d days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least d prior days of transaction data.

Given the value of d and a client's total daily expenditures for a period of n days, find and print the number of times the client will receive a notification over all n days.

Note: The median of a list of numbers can be found  by arranging all the numbers from smallest to greatest. If there is an  odd number of numbers, the middle one is picked. If there is an even  number of numbers, median is then defined to be the average of the two  middle values.

Input Format

The first line contains two space-separated integers denoting the respective values of n (the number of days there is transaction data for) and d (the number of prior days the bank uses to calculate median spending). 
 The second line contains n space-separated non-negative integers where each integer  i denotes expenditure (i.e., the client's total expenditure for day i).

Constraints 

Output Format

Print an integer denoting the total number of times the client receives a notification over a period of n days.

Sample Input 0 

9 5
2 3 4 2 3 6 8 4 5


Sample Output 0 

2


Explanation 0

We must determine the total number of notifications the client receives over a period of n = 9 days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data and notifications = 0. On the sixth day, the bank has d = 5 days of prior transaction data, {2,3,4,2,3}, and median=3 dollars. The client spends 6 dollars, which triggers a notification because 6 >= 2 x median. Thus, notifications = 1.

On the seventh day, the bank has d = 5 days of prior transaction data, {3,4,2,3,6}, and  median = 3 dollars. The client spends 8 dollars, which triggers a notification because 8 >= 2 x median. Thus, notifications = 1 + 1 = 2.

On the eighth day, the bank has d=5 days of prior transaction data, {4,2,3,6,8}, and median = 4 dollars. The client spends 4 dollars, which does not trigger a notification because 4 < 2 x median.

On the ninth day, the bank has d = 5 days of prior transaction data, {2,3,6,8,4}, and a transaction median of 4 dollars. The client spends 5 dollars, which does not trigger a notification because 5 < 2 x median.

We then print the final value of notifications (which is 2) as our answer.

Sample Input 1 

5 4
1 2 3 4 4


Sample Output 1 

0

Problem
An Arithmetic Progression is defined as one in which there is a  constant difference between the consecutive terms of a given series of  numbers.


You are provided with consecutive elements of an Arithmetic  Progression. There is however one hitch: exactly one term from the  original series is missing from the set of numbers which have been given  to you.


The rest of the given series is the same as the original AP.   Find the missing term.  


You have to write the function find_missing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.


Execution examples

1 3 7 9 11 


>5



27, -12, 66, 79, 14, 1, 92, 40 


>53


963, 1405, 1301, 950, 1028, 391, -12, 326, 222, 1249, 1067, 170, 937, 911, 664, 

651, 300, 1327, 14, 1171, 105, 274, 417, 1340, 547, 378, 53, 807, 1158, 638, 1197, 

248, 1379, 586, 1054, 794, 352, 404, 625, 209, 1106, 235, 1132, 1041, 456, 469, 573, 

183, 924, 1457, 1353, 1002, 755, 872, 118, 1314, 716, 1093, 1431, 729, 898, 885, 

677, 430, 1262, 1366, 1015, 742, 1236, 495, 534, 131, 313, 1184, 261, 976, 1418, 

40, 1288, 1496, 703, 27, 820, 1275, 287, 79, 859, 1223, 157, 781, 1080, 144, 599, 

1392, 989, 339, 768, 66, 1483, 1145, 508, 521, 1444, 1470, 1119, 92, 482, 365, 1210, 

443, 612, 833, 1, 560, 846, 690 


>196


Problem 
We have a string s
We have a number n

Create a function string_n_string(s, n) that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars to the back and return the result of the string after applying the function to it n times.


Example

string_n_string("Wow Example!", 1)
> "WwEapeo xml!"



string_n_string("qwertyuio",2)

> "qtorieuwy"