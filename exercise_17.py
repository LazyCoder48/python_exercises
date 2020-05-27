'''
Write a Python program to test whether a number is within 100 of 1000 or 2000
'''


def near_thousand(num):
    return ((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100))


print(near_thousand(1100))
print(near_thousand(1230))
print(near_thousand(2000))
print(near_thousand(1980))
