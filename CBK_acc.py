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

# i = input("What is your initial cost? ")
# s = input("What is your selling price? " ) 
# c = input("How much does one product cost to make? ") 

i = 1000 #initial cost
s = 60 #selling price 
c = 10 #cost, material and labour 

x = np.linspace(0,30,30)
y = s*x
z = c*x+i   # z = cost line 

xi = (i-0) / (s-c) # xi, yi; variables for plotting point of intercept
yi = c * xi + i 

    

plt.plot(x, y, z, '-r') 
plt.title('CBK shirts, Income/Cost relationship')

plt.xlabel('No. shirts made/sold')
plt.ylabel('Income/Cost')

print('Product amount to break Even:',xi) #prints number of products needed to sell to break even (first value I want to round up)

plt.scatter(xi,yi, color='black' ) #plots black dot on grid for POI
plt.savefig("two_straight_lines_intersection_point_02.png", bbox_inches='tight') #saves model

plt.grid() #generates grid? 
plt.show() #shows image? 




