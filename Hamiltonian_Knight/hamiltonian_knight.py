"""Script to solve the Hamiltonian Knight Problem"""
import sys
import networkx as nx
import matplotlib.pyplot as plt

def main():
	""" Main Entry"""
	
	G_knight = nx.Graph()

	knight_edge_list = create_knight_graph_edge_list(8)

	#print(knight_edge_list)

	G_knight.add_edges_from(knight_edge_list)

	G_knight = nx.to_directed(G_knight)

	hp = nx.algorithms.tournament.hamiltonian_path(G_knight)

	#print(hp)


	nx.draw_networkx(G_knight)
	plt.show()

	#input("Press Enter to continue...")


def create_knight_graph_edge_list(side_length):
	l = []

	for i in range(0, side_length-1): # Column
		for j in range(0, side_length-1): # Row
			for di in [-1,1]:
				for dj in [-2,2]:
					if within_boundary(i+di, j+dj, side_length):
						l.append([vertex_name(i, j, side_length), \
							vertex_name(i+di, j+dj, side_length)])
						#l.append([vertex_name(i+di, j+dj, side_length), \
						#	vertex_name(i, j, side_length)])
			for di in [-2,2]:
				for dj in [-1,1]:
					if within_boundary(i+di, j+dj, side_length):
						l.append([vertex_name(i, j, side_length), \
							vertex_name(i+di, j+dj, side_length)])
						#l.append([vertex_name(i+di, j+dj, side_length), \
						#	vertex_name(i, j, side_length)])

	return l

def within_boundary(i, j, side_length):
	return i >= 0 and i < side_length and j >= 0 and j < side_length

def vertex_name(i, j, side_length):
	#eturn i + j * side_length
	return (i,j)


if __name__ == '__main__':
	sys.exit(main())
