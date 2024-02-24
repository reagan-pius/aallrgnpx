"""
Then write a program that lets the user type in an integer and that keeps calling collatz() 
on that number until the function returns the value 1. 
(Amazingly enough, this sequence actually works for any integer—sooner or later, 
using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.
Your program is exploring what’s called the Collatz sequence, sometimes called
“the simplest impossible math problem.”)
"""

import time

def collatz(number):
    if number % 2 == 0:  # If the number is even
        result = number // 2
    else:  # If the number is odd
        result = 3 * number + 1
    
    time.sleep(0.1)
    print(result)  # Print the result
    return result  # Return the result

def main():
    try:
        user_input = int(input("Enter a number: "))  # Ask the user for an integer input
        while user_input != 1:  # Continue calling collatz until the result becomes 1
            user_input = collatz(user_input)  # Call the collatz function with the user's input
    except ValueError:
        print("Please enter a valid integer.")  # Handle non-integer input

if __name__ == "__main__":
    main()