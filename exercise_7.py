'''
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output: java
'''
file_name = input('Enter file name with extension, example: abc.java')
if file_name == '':
    file_name = 'abc.java'
name = file_name.split('.')[0]
ext = file_name.split('.')[-1]

print(ext)
