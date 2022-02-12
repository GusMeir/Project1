###############################################################################################################################
import numpy as np
import matplotlib.pyplot as plt
###############################################################################################################################
initial_cost = 26 
shirtcost = 10  # 2 + every 100 shirts 
shirtprice = 20
###############################################################################################################################
# n = shirtcost 
# x_axis = "number of shirts"
# y_axis = "Cost/Income" 

i = 26 #initial cost
s = 20 #selling price 
c = 10 #cost, material and labour 


x = np.linspace(0,30,30)
y = s*x
z = c*x+i
plt.plot(x, y, z, '-r') 
plt.title('CBK shirts, Income/Cost relationship')

plt.xlabel('No. shirts made/sold')
plt.ylabel('Income/Cost')

plt.grid()
plt.show() 
