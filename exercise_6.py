'''
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
input = '3, 5, 7, 23'
num_list = input.split(',')
num_tuple = tuple(num_list)
print(num_list)
print(num_tuple)