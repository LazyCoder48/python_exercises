'''
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
'''
def sum_all(x, y, z):
    if x == y == z:
        return (x+y+z)*2
    else:
        return (x + y + z)


print(str(sum_all(5, 5, 5)))
print(str(sum_all(1, 2, 3)))
