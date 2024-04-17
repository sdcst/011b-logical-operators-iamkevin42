#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

def is_divisible_by_6_not_8(num):
    if num % 6 == 0:
        if num % 8 != 0:
            return True
        else:
            return False
    else:
        return False

number = int(input("Enter a number\n"))
if is_divisible_by_6_not_8(number):
    print(number, "is frue")
else:
    print(number, "is not frue")

