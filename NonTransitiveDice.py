'''
Find first non-repeating character in a string
'''

def firstNotRepeatingCharacter(s):
    seen=""
    for i in s:
        if i not in seen:
            seen=seen+i
            #print(seen)
            if s.count(i)==1:
                return i
    return "_"

s=input("Please enter an input string: ")
print("Output is : ", firstNotRepeatingCharacter(s))