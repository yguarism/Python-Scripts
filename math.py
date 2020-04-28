# Simple Program to Learn some of the MatPlotLib functionality
# Help Visualize 3D Lines and Planes for Gr. 11 IB Math Tutoring Questions


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def make_plane(ax, a,b,c,d, color):
	x = np.linspace(-10,10,100)
	y = np.linspace(-10,10,100)

	X,Y = np.meshgrid(x,y)
	Z = (d - a*X - b*Y) / c
	surf = ax.plot_surface(X, Y, Z, color=color)

def make_line_vectorform (ax, v1, d, color):
	t = np.linspace(-10, 10, 100)
	x = v1[0] + d[0]*t
	y = v1[1] + d[1]*t
	z = v1[2] + d[2]*t
	ax.plot(x,y,z, color=color)

def make_line_2points(ax,x,y,z, color, label):
	ax.plot(x,y,z, color=color, label=label)

def q_11_1 (ax):
	make_line_2points(ax,[1,-3],[2,1],[1,4], 'black', 'AB')
	make_line_2points(ax,[-3,5],[1,-1],[4,2], 'red', 'BC')
	make_line_2points(ax,[1,5],[2,-1],[1,2], 'green', 'AC')
	make_line_2points(ax,[1,5],[2,3],[1,7], 'blue', 'AD')
	make_line_2points(ax,[-3,5],[1,3],[4,7], '#592D00', 'BD')
	make_line_2points(ax,[5,5],[-1,3],[2,7], 'purple', 'CD')

def q_11_2 (ax):
	make_line_2points(ax,[4,0],[0,0],[0,0], 'black', 'AO')
	make_line_2points(ax,[0,0],[6,0],[0,0], 'red', 'BO')
	make_line_2points(ax,[0,0],[0,0],[-2,0], 'green', 'CO')
	make_line_2points(ax,[4,0],[0,6],[0,0], 'blue', 'AB')
	make_line_2points(ax,[0,0],[6,0],[0,-2], '#592D00', 'BC')
	make_line_2points(ax,[4,0],[0,0],[0, -2], 'purple', 'CA')

def main():
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	q_11_1(ax)
	#q_11_2(ax)

	#make_line_vectorform(ax, [1,1,1], [1,-1,3], "blue")
	#make_line_vectorform(ax, [1,1,1], [2,-8,5], "green")
	#make_plane(ax, 1, -1, 3, -10, '#add8e6')
	#make_plane(ax, 2, -8, 5, 18,'#ade6bb')
	#make_line_vectorform(ax, [2,-1,3], [1,-1,3], "green")
	plt.legend()
	plt.show()

# x_p = np.linspace(-1,10,20)
# y_p = np.linspace(-1,10,20)

# X_p, Y_p = np.meshgrid(x_p, y_p)
# Z_p = (-3 + 7*X_p + 2*Y_p)/3

# surf = ax.plot_surface(X_p, Y_p, Z_p)

main()
