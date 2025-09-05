"""
main.py - Collaborative Coding Project
Group ID: 6

Each contributor adds ONE function in this file.
- Include a proper docstring
- Add an Author tag
- Keep your code within your assigned section
"""

# ==============================
# Contributor A Function
# ==============================
# TODO: Contributor A adds their function here
# Example format:
# def function_a(...):
#     """
#     Brief description
#
#     Args:
#         param: explanation
#
#     Returns:
#         type: explanation
#
#     Author:
#         Name (Roll No.)
#     """
#     pass


# ==============================
# Contributor B Function
# ==============================
# TODO: Contributor B adds their function here
def addn(a, b):
    return a + b


addn(2, 3)


# ==============================
# Contributor C Function
# ==============================
# TODO: Contributor C adds their function here
def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: remove spaces and make lowercase
    s = s.replace(" ", "").lower()

    # Compare string with its reverse
    return s == s[::-1]


# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# ==============================
# Contributor D Function
# ==============================
# TODO: Contributor D adds their function here


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)


# ==============================
# Driver / Integration Function
# ==============================
def main():
    """
    Driver function that calls all contributed functions
    in a meaningful sequence. To be completed by Admin
    once all modules are ready.
    """
    print("=== Collaborative Project Demo ===")
    # Example (to be updated later):
    # result_a = function_a(...)
    # print("Function A result:", result_a)


if __name__ == "__main__":
    main()
