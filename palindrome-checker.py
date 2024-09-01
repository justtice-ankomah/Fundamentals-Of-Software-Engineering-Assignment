def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Get user input
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
