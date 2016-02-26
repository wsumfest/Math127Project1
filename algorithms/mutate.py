from numpy import linalg as LA
import numpy as np
import multiprocessing as mp
from functools import partial
import subprocess
import time

#Super class for our phylogenetic tree
class Tree(object):

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def add_vertex(self,v1):
        self.vertices.append(v1)

    def add_edge(self,edge):
        self.edges.append(edge)


#Class that represents a node in our phylogenetic tree
class PhylogeneticNode(object):

    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence

    def set_dna_sequence(self,dna):
        self.dna_sequence = dna

    def get_sequence(self):
        return self.dna_sequence

    @staticmethod
    def calculate_distance(node1,node2):
        dna1 = node1.get_sequence()
        dna2 = node2.get_sequence();
        different_characters = 0
        assert(len(dna1) == len(dna2))
        for i in range(0,len(dna1)):
            if dna1[i] != dna2[i]:
                different_characters += 1
        return different_characters

#Class that we will be constructing when we call our mutate function
class PhylogeneticTree(Tree):

    def __init__(self, vertices, edges, root_node=None):
        self.vertices = vertices
        self.edges = edges
        self.root_node = root_node
        if root_node:
            self.vertices.append(root_node)

    def get_root_node(self):
        return self.root_node

    def set_root_node(self, node):
        if node not in self.get_vertices():
            self.add_vertex(node)
        self.root_node = node


#Class that simulates a Markov Chain
class MarkovChain(object):

    def __init__(self, transition_matrix, time):
        self.transition_matrix = transition_matrix
        self.time = time

    def get_transition_matrix(self):
        return self.transition_matrix

    def set_transition_matrix(self):
        power_matrix = LA.matrix_power(self.transition_matrix, self.time)
        self.transition_matrix = power_matrix

    def apply_to_char(self, char):
        assert(char == 'a' or char == 'c' or char == 't' or char == 'g')
        char_map = {"a": 0, "c": 1, "g": 2, "t": 3}
        index = char_map[char]
        base_vector = [.25, .25, .25, .25] #Assume uniform probability for bases in DNA
        power_matrix = self.transition_matrix
        transformation_vector = power_matrix[index]
        new_char = np.random.choice(char_map.keys(), p=transformation_vector)
        return new_char



def mutate(alpha, time, dna_sequence, threads):
    #We construct our phylogenetic tree here, as well as declare the root node
    root = PhylogeneticNode(dna_sequence)
    tree = PhylogeneticTree([],[], root)

    #sets maximum number of processes for our final implementation
    # proc = subprocess.Popen(["sysctl", "-n", "hw.ncpu"], stdout=subprocess.PIPE)
    # #truncate last char == '\n'
    # maximum_processes = int(proc.stdout.read()[:-1])


    #Use as Pool of processes for multithreaded programming
    pool = mp.Pool(processes=threads)

    transition_matrix = build_transition_matrix(alpha)

    while time > 0:
        markov_chain = MarkovChain(transition_matrix, 1)
        markov_chain.set_transition_matrix()
        my_func = partial(alias, markov_chain=markov_chain)

        #Apply instance method over that dna_sequence with pool.map
        new_seq = "".join(pool.map(my_func, dna_sequence))
        next_node = PhylogeneticNode(new_seq)
        phylo_dist = PhylogeneticNode.calculate_distance(root,next_node)
        if (phylo_dist != 0):
            tree.add_vertex(next_node)
            tree.add_edge([(root,next_node), phylo_dist])
            root = next_node
        transition_matrix = markov_chain.get_transition_matrix()
        time -= 1

    return tree

def build_transition_matrix(alpha):
    vector1 = [(1 -(3*alpha)), alpha, alpha, alpha]
    vector2 = [alpha, (1 -(3*alpha)), alpha, alpha]
    vector3 = [alpha, alpha, (1 -(3*alpha)), alpha]
    vector4 = [alpha, alpha, alpha, (1 -(3*alpha))]
    transition_matrix = [vector1, vector2, vector3, vector4]
    return transition_matrix


#Alias function that allows instance method for markov chain to be pickled for multiprocessing
def alias(arg, markov_chain):
    return markov_chain.apply_to_char(arg)


