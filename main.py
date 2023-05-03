import numpy as np
from matplotlib import pyplot as plt

#   Loading data and colormap
data = np.load('data/sdss_galaxy_colors.npy')
cm = plt.get_cmap('YlOrRd')

#   Creating color indexes
ug = data['u'] - data['g']
ri = data['r'] - data['i']

#   Defining color scale based on galaxy redshift and creating the scatter plot
reds = np.array(data['redshift'])
plot = plt.scatter(ug, ri, s=3, linewidth=0, c=reds, cmap=cm) 

#   Setting the plot colors, main and axis titles and the values
cb = plt.colorbar(plot)
cb.set_label('Redshift')
plt.title('Redshift(colour) u-g versus r-i')
plt.xlabel('Colour index u-g')
plt.ylabel('Colour index r-i')
plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 1)
plt.show()