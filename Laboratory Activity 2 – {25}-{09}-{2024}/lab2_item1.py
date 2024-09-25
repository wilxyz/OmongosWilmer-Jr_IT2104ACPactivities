def a_palindrome(num):

    str_num = str(num)

    if str_num == str_num[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
num = int(input("Enter an integer: "))

result = a_palindrome(num)
print(result)
