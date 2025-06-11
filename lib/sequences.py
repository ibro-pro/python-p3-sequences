#!/usr/bin/env python3

# Function to print Fibonacci sequence
def print_fibonacci(length):
    if length <= 0:
        print([])  # Return empty list if length is 0 or negative
        return
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    print(fib[:length])  

# Example usage
print("Fibonacci Sequence:")
print_fibonacci(7)  

# Lists
print("\nLists:")
s = [4, 6, 3, 9, 3, 5, 1, 2]
print(s[-2:])          
s.insert(2, 99)        
print(s)

# Tuples
print("\nTuples:")
months = ("Jan", "Feb", "Mar")
print(months[1])       

# Ranges
print("\nRanges:")
for i in range(2, 10, 2):
    print(i)           

# Strings
print("\nStrings:")
text = "hello"
print(text.upper())    
print(text[1:4])       
