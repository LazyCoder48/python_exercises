'''
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
print('Enter radius of cirlce')

radius = input()
try:
    radius = float(radius)
except ValueError:
    print('Please enter numerical values')
else:
    radius = float(radius)
area = float(0)
area = (22/7)*(radius**2)
print(str(area))
# print(str(float(area)))
# 14
