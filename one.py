#comment in python
# a='atmiya'
# print(a)
# b='rajkot'
# print(b)

# print('hi'*3)
# print('This will be printed on \n new line')

# city='morbi'
# city1='rajkot'
# print('city is :'+city)
# print('city is :',city1)

#Formatting output using format string
# city='surat'
# print('city is :%s'%city)
# print('city is :(%20s)'%city)
# print('city is :(%-20s)'%city)

#.format or {} placeholder
# a=1
# b=2
# print('There Value are :{0},{1}and{0}'.format(a,b))
# print('There Value are :{0},{1}and{0}'.format(b,a))
# print('{0} IS THE ONE AMONG THE BEST UNI'.format('atmiya uni'))

# Taking input from the user
# age=input('Enter the age :')
# print(age)
# print(type(age))

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()