from numpy import linalg as LA
import numpy as np
import multiprocessing
from functools import partial
import subprocess
import time
import pdb
import gc
import scipy



#Super class for our phylogenetic tree
class Tree(object):

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def add_node(self, v1):
        self.nodes.append(v1)

    def add_edge(self, node1, node2):
        tup = (node1, node2, node1.calculate_distance(node2))
        self.edges.append(tup)

    def __str__(self):
        return


#Class that represents a node in our phylogenetic tree
class PhylogeneticNode(object):

    number = 1

    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence
        self.number = PhylogeneticNode.number
        PhylogeneticNode.number += 1

    def set_dna_sequence(self,dna):
        self.dna_sequence = dna

    def get_sequence(self):
        return self.dna_sequence

    def calculate_distance(self,node2):
        dna1 = self.get_sequence()
        dna2 = node2.get_sequence()
        different_characters = 0
        assert(len(dna1) == len(dna2))
        for i in range(0,len(dna1)):
            if dna1[i] != dna2[i]:
                different_characters += 1
        return different_characters

    def __str__(self):
        return str(self.number)


def mutate_module(matrix, origin_seq, threads=1):
    manager = multiprocessing.Manager()
    new_seq = []
    jobs = []
    origin = []

    man_list = manager.list(origin_seq)
    dna_len = len(man_list)

    for i in range(0, dna_len):
        origin.append(origin_seq[i])

    curr_thread, bottom_index, top_index, len_of_block = 1,0, (dna_len//threads), (dna_len//threads)
    while curr_thread <= threads:
        if curr_thread == threads:
            top_index = dna_len
        np.random.seed()
        current_thread = multiprocessing.Process(target=mutate, args=(matrix, man_list, top_index, bottom_index))
        jobs.append(current_thread)
        current_thread.start()
        bottom_index = top_index
        top_index += len_of_block
        curr_thread += 1


    for job in jobs:
        job.join()
    del jobs
    
    for val in man_list:
        new_seq.append(val)


    origin = "".join(origin)
    origin_node = PhylogeneticNode(origin)

    # pdb.set_trace()

    new_node = PhylogeneticNode(new_seq)

    node_heur = determine_heurestic(origin_node, new_node)

    if node_heur != -1:

        return new_node

    return -1



def mutate(matrix, dna_list, top_index, bottom_index):
    char_map = {"A": 0, "C": 1, "G": 2, "T": 3}

    ###THIS WAS THE WORST BUG EVER GAAAAHHHHHHH####
    np.random.seed()
    
    # pdb.set_trace()

    for i in range(bottom_index, top_index):
        try:
            char = dna_list[i]
            index = char_map[char]
            transformation_vector = matrix[index]
            choice = np.random.rand(1,1)
            if choice <= transformation_vector[0]:
                new_char = 'A'
            elif choice <= transformation_vector[0] + transformation_vector[1]:
                new_char = 'C'
            elif choice <= transformation_vector[0] + transformation_vector[1] + transformation_vector[2]:
                new_char = 'G'
            else:
                new_char = 'T'

            dna_list[i] = new_char
            del choice
        except IndexError:
            print i
            print top_index
            print len(dna_list)
            break

    return

    


def determine_heurestic(origin_node, mutated_node):
    seq_len = len(origin_node.get_sequence())
    different_characters = PhylogeneticNode.calculate_distance(origin_node, mutated_node)

    if float(different_characters)/float(seq_len) > 0.05:
        return 1

    return -1



#alpha must be in [0.00, 0.33]
def build_transition_matrix(alpha):
    vector1 = [(1 -(3*alpha)), alpha, alpha, alpha]
    vector2 = [alpha, (1 -(3*alpha)), alpha, alpha]
    vector3 = [alpha, alpha, (1 -(3*alpha)), alpha]
    vector4 = [alpha, alpha, alpha, (1 -(3*alpha))]
    transition_matrix = [vector1, vector2, vector3, vector4]
    return transition_matrix



def simulate_evolution(dna_sequence, alpha, time, dt, threads=1):
    tree = Tree([PhylogeneticNode(dna_sequence)], [])
    transition_matrix = build_transition_matrix(alpha)
    power_matrix = LA.matrix_power(transition_matrix, dt)

    while time > 0:
        i = 0
        fixed_length = len(tree.get_nodes())
        node_list = tree.get_nodes()
        if fixed_length > 10:
            return tree

        while i < fixed_length:
            node = node_list[i]
            origin_sequence = node.get_sequence()
            wrapper = list(origin_sequence)
            next_node = mutate_module(power_matrix, wrapper, threads=threads)

            if next_node != -1:
                tree.add_node(next_node)
                tree.add_edge(node, next_node)

            gc.collect()
            i += 1
        time -= dt
        print time

    return tree


