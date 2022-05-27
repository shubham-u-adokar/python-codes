# By Shubham Adokar
# Write a program to accept a string from the user and display characters that are present at an even index number.

# Input:
# str = "pynative"
# Output:
# Orginal String is : pynative
# Printing only even index chars
# p
# n
# t
# v

input_string = input("Str = ")
print(f"Orginal String is : {input_string}")
print("Printing only even index chars")
for i in range (len(input_string)):
    if i % 2 == 0:
        print(input_string[i])