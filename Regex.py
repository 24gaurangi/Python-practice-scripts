'''
This function validates input string against a regex
'''

def SimpleSymbols(str): 
    valid='true'
    for i in range(len(str)-1):
        if i==0 and str[i].isalpha():
            return 'false'
        elif str[i].isalpha() and valid=='true':
            if str[i-1]=='+' and str[i+1]=='+':
                valid='true'
            else:
                valid='false'
                
    return valid

print SimpleSymbols(input()) 