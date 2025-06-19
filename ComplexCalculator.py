"""imports the os and time modules from the Python Standard Library.
The os module provides a way of using operating system dependent functionality,
like reading or writing to the file system.
The time module provides various time-related functions, like getting the current
time or pausing the execution of the script."""

import os
import time


def addition():
    user_input = input()
    if not user_input.strip():
        raise ValueError("No input provided")
    numbers = list(map(int, user_input.split()))
    print(sum(numbers))



def subtraction():
    """This function asks the user to enter two numbers.
    It then subtracts the second number from the first and returns the result."""
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))

    return n_1 - n_2


def multiplication():
    """
    Function asks user to enter a series of numbers separated by spaces.
    Multiplies all the numbers together and returns the result.

    Returns:
        int or str: Product of the numbers or "Invalid entry" if input is invalid.
    """
    try:
        input_str = input("Enter all numbers separated by space: ").strip()
        if not input_str:
            raise ValueError("Empty input")

        nums = list(map(int, input_str.split()))
        if not nums:
            raise ValueError("No valid numbers provided")

        result = 1
        for num in nums:
            result *= num

        print(result)
        return result

    except (ValueError, TypeError):
        print("Invalid entry")
        return "Invalid entry"




def average():
    """This function takes space separated number series and then convert it to a list.
    Then calculates the average of that list of numbers."""

    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums) / len(nums)


def factorial(num):
    """
    Function to calculate the factorial of a non-negative integer.

    Args:
        num (int): A non-negative integer.

    Returns:
        int: Factorial of the number.

    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")

    if num < 0:
        raise ValueError("factorial is undefined for negative numbers")

    answer = 1
    for i in range(1, num + 1):
        answer *= i

    return answer



def complex_addition():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    real_sum = 0
    imag_sum = 0
    for i in range(0, len(nums) - 1, 2):
        real_sum += nums[i]
    for i in range(2, len(nums) - 1, 2):
        imag_sum += nums[i]
    imag_sum += nums[-1]
    return f"{real_sum}+ i{imag_sum}"


def complex_subtraction():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    real_sub = nums[0]
    imag_sub = nums[1]
    for i in range(2, len(nums) - 1, 2):
        real_sub -= nums[i]
    for i in range(3, len(nums) - 1, 2):
        imag_sub -= nums[i]
    imag_sub -= nums[-1]
    return f"{real_sub}+ i{imag_sub}"


def complex_multiplication():
    nums = list(map(int, input("Enter 4 numbers separated by space (a b c d): ").split()))
    real = nums[0] * nums[2] - nums[1] * nums[3]
    imag = nums[0] * nums[3] + nums[2] * nums[1]
    return f"{real}+ i{imag}"


def complex_division():
    nums = list(map(int, input("Enter 4 numbers separated by space (a b c d): ").split()))
    denominator = nums[2] ** 2 + nums[3] ** 2
    real = (nums[0] * nums[2] + nums[1] * nums[3]) / denominator
    imag = (nums[1] * nums[2] - nums[0] * nums[3]) / denominator
    return f"{real}+ i{imag}"


from math import factorial

def binomial(num):
    """
    Calculate the binomial coefficient C(n, k) = n! / (k! * (n-k)!)
    
    Args:
        num (tuple or list): Two integers (n, k), where n >= k >= 0.
    
    Returns:
        int: Binomial coefficient.
    
    Raises:
        ValueError: If inputs are not valid or k > n.
    """
    # Input validation
    if not isinstance(num, (list, tuple)) or len(num) != 2:
        raise ValueError("Input must be a tuple or list of two integers.")
    
    n, k = num

    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("Both n and k must be integers.")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative integers.")
    if k > n:
        raise ValueError("k must be less than or equal to n.")
    
    # Use integer division to avoid float precision issues
    return factorial(n) // (factorial(k) * factorial(n - k))


