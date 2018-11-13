#n1=0
#s1=""
#index1 = []
def my_sort(numbers):
    return sorted(numbers, key=lambda v: (v%2==1, v))
    
def string_n_string(s,n):
    for i in range(n): 
        index = my_sort(range(len(s))) 
        s = ''.join([s[i] for i in index])

    print s

#string_n_string("Wow Example!",1)
#string_n_string("qwertyuio",2)
string_n_string("Such Wow!",1)
