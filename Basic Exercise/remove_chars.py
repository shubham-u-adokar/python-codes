# By Shubham Adokar
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Input:
# String = pynative
# Number of characters to be removed = 4
# Output:
# The remainging sting is : tive

def remove_chars(string, chars):
    return string[int(chars):]

if __name__ == '__main__':
    string = input("String = ")
    chars = input("Number of characters to be removed = ")
    print(remove_chars(string, chars))