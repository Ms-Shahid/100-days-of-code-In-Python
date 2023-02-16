#Data Types

string = "Hello"[0]
print(string) 

print("123" + "345") #concatenation

print(100 + 151) #Integer addition

large_numbers = 123_456_789 #seperated with commans 
print(large_numbers)

#floating numbers 
pi = 3.14566
print(pi)

#Boolean 
bool = True | False
print(bool)

mystery = 734_529.678
print(type(mystery))

#Type Error & type checking

num_char = len(input("enter something! "))
print(type(num_char))

#int to str
new_num_char = str(num_char)
print(type(new_num_char))

#int to float
var = float(123)
print(type(var))

#float to int
fl = int(6.6578)
print(type(fl))

print(80 + float("100.34")) #convert to str -> float

two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number))

seperate_into_ints = int(two_digit_number[0]) + int(two_digit_number[1]) #str to int

print(seperate_into_ints)
print(type(seperate_into_ints))