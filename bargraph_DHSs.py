# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Fake dataset
height = [86, 865, 844, 1000, 2955, 12315]
bars = ('Sperm', 'oocyte', '1 cell', '2 cell', '4 cell', '8 cell')
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('All DHSs')
plt.xlabel('Stages')
plt.ylabel('Number of DHSs')
 
# Limits for the Y axis
#plt.ylim(0,60)
 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()
