import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file.csv')

# extracting the id and sales into variables x and y 
x= df['id']
y= df['salary']

# creating the line graph using bar()
plt.bar(x, y, label=' production Department', color='red')

# setting labels for x-axis and y-axis 
plt.xlabel('id')
plt.ylabel('salary')

# setting title and labels
plt.title('Department data')

# showing the legend 
plt.legend()

# display the graph
plt.show()
