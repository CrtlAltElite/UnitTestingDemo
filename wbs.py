# given a string return the first consentant letter of the string, if not con return false
def firstc(string):
    for letter in string:
        if letter.isalpha() letter.lower() not in {'a','e','i','o','u'}:
            return letter
    return False

# return the Sum of the digits of an integer
# n will always be an integer
def numsum(n):
    total=0
    for c in str(n):
        total+=int(c)
    return total