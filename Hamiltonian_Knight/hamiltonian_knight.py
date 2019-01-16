"""Script to solve the Hamiltonian Knight Problem"""
import sys
import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

def main():
	""" Main Entry"""
	
	BOARD_WIDTH = 5

	G_knight = create_knight_graph(BOARD_WIDTH)

	pos_layout = {}
	for n in G_knight:
		pos_layout[n] = n


	hp = nx.algorithms.tournament.hamiltonian_path(G_knight)

	hp = find_hamiltonian_cycle(G_knight)

	print("Diameter: " + str(nx.diameter(G_knight)))

	nx.draw(G_knight, pos=pos_layout)
	#plt.show()

	#input("Press Enter to continue...")

def create_knight_graph(side_length):
	G_knight = nx.Graph()

	knight_edge_list = create_knight_graph_edge_list(side_length)

	G_knight.add_edges_from(knight_edge_list)

	G_knight = nx.to_directed(G_knight)

	return G_knight


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

def find_hamiltonian_cycle(G):
	n = list(G.nodes)[0]
	m = list(G.neighbors(n))[0]

	paths = nx.all_simple_paths(G, n, m, cutoff=nx.number_of_nodes(G))

	hp = max(list(paths), key=len)
	
	print("Path :" + str(hp))
	print("Length :" + str(len(hp))) # Not the longest path in G because a specific node was chosen



if __name__ == '__main__':
	sys.exit(main())
