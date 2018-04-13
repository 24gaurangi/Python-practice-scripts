'''
This function returns the first longest word from the input string
'''

def LongestWord(sen): 
    max=0
    st=""
    for c in sen:
        if c.isalnum():
            st=st+c
        else:
            st=st+" "
    words=st.split(" ")
    for word in words:
        if len(word) > max:
            max=len(word)
            longestword=word
    return longestword
 
print LongestWord(input("Please enter a string\n"))