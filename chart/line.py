import matplotlib.pyplot as plt
over = [10,20,30,40,50]

team_a = [100,250,275,300,450]
team_b = [80,150,250,350,425]

# creating the line graph using plot()
plt.plot(over, team_a , color = "blue")
plt.plot(over, team_b , color = "red")

# setting title and labels 
plt.title('Tunament')

# showing the legend 
plt.legend()

# display the graph
plt.show()
