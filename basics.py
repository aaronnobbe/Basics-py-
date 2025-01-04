# Python Basics 
# 1. Reverse a String
def reverse_string(s):
    return s[::-1]

# 2. Sum of a List of Numbers
def sum_of_list(numbers):
    return sum(numbers)

# 3. Find the Largest Number in a List
def largest_number(numbers):
    return max(numbers)

# 4. Check if a Number is Even or Odd
def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# 5. Count the Occurrences of a Character in a String
def count_character(s, char):
    return s.count(char)

# 6. Generate a List of Squares of Numbers
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# 7. Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

# 8. Check for Balanced Parentheses
def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# 9. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 10. Linear Search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# 11. Binary Search (requires sorted list)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 12. Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# Unified Input Handling
print("Welcome to the Python Basics Program!")

# Reverse String
string_to_reverse = input("Enter a string to reverse: ")
print("Reversed String:", reverse_string(string_to_reverse))

# Sum and Largest Number
numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sum of List:", sum_of_list(numbers_list))
print("Largest Number:", largest_number(numbers_list))

# Even or Odd Check
number = int(input("Enter a number to check if it's even or odd: "))
print(f"The number {number} is {is_even_or_odd(number)}.")

# Character Count
string_to_check = input("Enter a string to check: ")
character_to_count = input("Enter the character to count: ")
print(f"The character '{character_to_count}' appears {count_character(string_to_check, character_to_count)} times in '{string_to_check}'.")

# Squares Generation
n = int(input("Enter a number to generate squares up to: "))
print(f"Squares of numbers from 1 to {n}:", generate_squares(n))

# Palindrome Check
string_to_check = input("Enter a string to check if it's a palindrome: ")
print(f"Is '{string_to_check}' a palindrome?", is_palindrome(string_to_check))

# Check for Balanced Parentheses
parentheses_string = input("Enter a string to check for balanced parentheses: ")
print(f"Is the string '{parentheses_string}' balanced?", is_balanced(parentheses_string))

# Bubble Sort
numbers_list = list(map(int, input("Enter numbers separated by spaces to sort (Bubble Sort): ").split()))
print("Sorted List (Bubble Sort):", bubble_sort(numbers_list))

# Linear Search
target = int(input("Enter a number to search for (Linear Search): "))
index = linear_search(numbers_list, target)
if index != -1:
    print(f"Number found at index {index}.")
else:
    print("Number not found.")

# Binary Search
numbers_list.sort()  # Ensure the list is sorted for binary search
print("Sorted List for Binary Search:", numbers_list)
target = int(input("Enter a number to search for (Binary Search): "))
index = binary_search(numbers_list, target)
if index != -1:
    print(f"Number found at index {index}.")
else:
    print("Number not found.")

# Merge Two Sorted Lists
list1 = list(map(int, input("Enter the first sorted list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second sorted list of numbers separated by spaces: ").split()))
merged_list = merge_sorted_lists(list1, list2)
print(f"Merged and Sorted List: {merged_list}")
