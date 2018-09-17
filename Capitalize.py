'''
This program takes the input string and capitalizes first letter of every word in the string
'''
# Naive approach

def LetterCapitalize(str):
    new_str=""
    cc=False
    for i in range(len(str)):
        if i == 0:
            new_str=new_str + str[i].upper()
        elif str[i] == " ":
            cc=True
            new_str=new_str + str[i]
        elif cc:
            new_str=new_str + str[i].upper()
            cc=False
        else:
            new_str=new_str + str[i]
    return new_str


print(LetterCapitalize(input("Please enter a string to capitalize\n")))

