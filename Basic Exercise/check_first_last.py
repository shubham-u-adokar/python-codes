# By Shubham Adokar
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Input:
# Enter list elements (comma ',' seperated) = 10,20,30,40,10
# Output:
# First and last element of list are same & value is 10.

def check_first_last(numbers_list):
    return numbers_list[0] == numbers_list[-1]

if __name__ == '__main__':
    input_number_list = input("Enter list elements (comma ',' seperated) = ").split(",")
    for i in input_number_list:
        i = int(i)
    if check_first_last(input_number_list):
        print("First and last element of list are same")
    else:
        print("First and last element of list are not same")