from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# x = [5, 2, 9, 4, 7]
# y = [10, 5, 8, 4, 2]
#
# # Function to plot
# plt.plot(x, y)
# plt.show()
#
# plt.bar(x, y)
# plt.show()
#
# plt.hist(y)
# plt.show()
#
# plt.scatter(x, y)
# plt.show()

# # fig = plt.figure()
# # ax = plt.axes(projection="3d")
# plt.figure()
# plt.axes(projection="3d")
# plt.show()
#
# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 1, 4, 9, 16, 25, 36]
# z = [0, 1, 4, 9, 16, 25, 36]
# ax = plt.axes(projection="3d")
# # ax.plot3D(x, y, z, 'red')
#
# ax.scatter(x,y,z)
# plt.show()

plt.figure()
ax = plt.axes(projection="3d")

# Grab some test data.
X, Y, Z = mplot3d.axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()