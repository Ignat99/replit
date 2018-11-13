open F, ">2.txt";
$/=\0;$_=<>;
for(split/\s|\,|\.|\;|\:|\'|\"|\!|\?/,$_){print F$_,' ' if($_ eq reverse$_)}


def remove_signs(s):
    s = s.lower()
    signs = "?!. \'\"`,:;-_/()[]~\n"
    s_without_signs = ""
    for letter in s:
        if letter not in signs:
            s_without_signs += letter
    return s_without_signs


with open('palindromes.txt', 'r')as f:
    for line in f:
        text = remove_signs(line)
        if text == text[::-1]:
            print('Y', ' ')
        else:
            print('N', ' ')


from numpy import median
median([1, -4, -1, -1, 1, -3])

def rotate(l, n):
    return l[-n:] + l[:-n]
