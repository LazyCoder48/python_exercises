'''
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
'''


def difference(num):
    const = 17
    if num > const:
        print(str(abs(num - const) * 2))
    else:
        print(str(abs(num - const)))


difference(22)
difference(14)
