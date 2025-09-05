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
def addn(a,b):
    return a+b
add(2,3)


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


def div(a,b):
    return a//b


# Example usage



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
