# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Fake dataset
height = [12, 6, 2, 24, 18, 19, 3, 44, 58, 42, 299, 85, 3007]
bars = ('all', '1:2:8', '1:4', '1:4:8', '1:8', '1', '2:4', '2:4:8','2:8', '2', '4:8', '4', '8')
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('Stage combinations')
plt.xlabel('Groups')
plt.ylabel('Number of enhancers')
 
# Limits for the Y axis
#plt.ylim(0,60)
 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()
