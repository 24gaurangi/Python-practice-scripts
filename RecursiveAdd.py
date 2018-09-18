''' 
Simple program to recursively add numbers from 1 to input number 
'''

def recursiveAdd(num): 
    if num == 1:
        return 1
    else:
        return num + recursiveAdd(num-1)

print(recursiveAdd(int(input("Please input a number: "))))