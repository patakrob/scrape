
def is_msci_number(n):
    # Write your code here
    digits = list(str(n))
    temp_str = []
    print(digits)
    for i in digits:
        print(i, len(digits))
        temp_str.append(int(i)**len(digits))
    print(temp_str)
    msci = sum(temp_str)
    print(msci)
    if n == msci:
        is_msci = True
    else:
        is_msci = False

    return is_msci


def is_palindrome(n):
    # Write your code here
    if n == int(str(n)[::-1]):
        pal = True
    else:
        pal = False
    return pal

