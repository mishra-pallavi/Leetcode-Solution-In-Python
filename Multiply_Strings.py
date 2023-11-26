# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


def multiply(num1,num2):
    n1 = int(num1)
    n2 = int(num2)
    n3 = n1*n2
    return str(n3)


num1 = "2"
num2 = "3"
res = multiply(num1,num2)
print(type(res))
print(res)