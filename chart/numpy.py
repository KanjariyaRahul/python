#using numpy group bar garph 

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import xlrd


# # Read the Excel file
# df = pd.read_excel('stationary.xlsx')

# print(df)

# # Define years and extract sales data for 'pencil' and 'pen'
# years = [2021, 2022, 2023]
# x = df['pencil']
# y = df['pen']

# xaxis = np.arange(len(years))

# plt.bar(xaxis - 0.2, x, 0.4, label='pencil')
# plt.bar(xaxis + 0.2, y, 0.4, label='pen')

# plt.xticks(xaxis, years)  # Setting x-axis ticks to be years

# plt.xlabel('products')
# plt.ylabel('sales')
# plt.title('Sales of Products Over Years')
# plt.legend()
# plt.show()


#===========================
#seatter plot

# import matplotlib.pyplot as plt 
# import numpy as np

# x= np.random.randn(10)
# y= np.random.randn(10)

# plt.scatter(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('seatter Diagram')
# plt.show()


# =============================
#Area folt

import matplotlib.pyplot as plt 
import numpy as np
x=range(1,6)
y=(1,4,6,2,4)

plt.fill_between(x,y)
plt.title('Area flot')
plt.show()



