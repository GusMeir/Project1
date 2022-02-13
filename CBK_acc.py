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

xi = (i-0) / (s-c) # xi, yi; variables for plotting point of intercept
yi = c * xi + i 

x = np.linspace(0,30,30)
y = s*x
z = c*x+i       # z = cost line 

plt.plot(x, y, z, '-r') 
plt.title('CBK shirts, Income/Cost relationship')

plt.xlabel('No. shirts made/sold')
plt.ylabel('Income/Cost')

print('(xi,yi)',xi,yi) #prints number of products needed to sell to break even (first value I want to round up)

plt.scatter(xi,yi, color='black' ) #plots black dot on grid for POI
plt.savefig("two_straight_lines_intersection_point_02.png", bbox_inches='tight') 

plt.grid() #generates grid? 
plt.show() #shows image? 




