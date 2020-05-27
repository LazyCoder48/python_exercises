'''
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''


def replicate_string(str, n):
    final_string = ''
    for i in range(n):
        final_string = final_string + str
    return final_string


print(replicate_string('Hi! ', 3))
print(replicate_string('Oy!', 0))
print(replicate_string('Ay! ', 2) + 'Captain')
