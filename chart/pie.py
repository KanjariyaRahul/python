import matplotlib.pyplot as plt

stud = [24,36,29,11,10]
dep_name = ['Bca', 'Mca', 'Mba', 'bba','Ba']

# creating the line graph using pie()
plt.pie(stud,labels=dep_name) 

# setting title and labels
plt.title('Atmiya University')

# showing the legend 
plt.legend()

# display the graph
plt.show()
