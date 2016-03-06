from numpy import linalg as LA
import numpy as np
from multiprocessing.dummy import Process
from functools import partial
import subprocess
import time
import pdb
import threading

BEST_THREAD_LEVEL=2



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

    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence

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
        return self.get_sequence()


def mutate_module(matrix, node, threads=1):
    new_seq = []
    main_seq = list(node.get_sequence())
    dna_len = len(main_seq)
    curr_thread, bottom_index, top_index = 1,0, (len(main_seq)//threads)
    while curr_thread <= threads:
        if curr_thread == threads:
            top_index = dna_len
        sub_sequence = main_seq[bottom_index:top_index]
        current_thread = threading.Thread(target=mutate, args=(matrix, sub_sequence))
        current_thread.start() 
        bottom_index = top_index
        top_index *= 2
        curr_thread += 1
        try:
            current_thread.join()
        except RuntimeError:
            print "can't join thread"

        new_seq += sub_sequence

    new_seq = "".join(new_seq)

    new_node = PhylogeneticNode(new_seq)

    node_heur = determine_heurestic(node, new_node)

    if node_heur != -1:
        return new_node

    return -1



def mutate(matrix, dna_list):
    char_map = {"A": 0, "C": 1, "T": 2, "G": 3}

    #Apply instance method over that dna_sequence with pool.map
    for i in range(0, len(dna_list)):
        char = dna_list[i]
        index = char_map[char]
        transformation_vector = matrix[index]
        new_char = np.random.choice(char_map.keys(), p=transformation_vector)
        dna_list[i] = new_char
    
    thread = threading.current_thread()
    try:
        thread.join()

    except RuntimeError:
        return 


def determine_heurestic(origin_node, mutated_node):
    seq_len = len(origin_node.get_sequence())
    different_characters = PhylogeneticNode.calculate_distance(origin_node, mutated_node)

    if different_characters > (seq_len // 200):
        return 1

    return -1



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
        while i < fixed_length:
            node = tree.get_nodes()[i]
            next_node = mutate_module(power_matrix, node, threads=threads)
            if next_node != -1:
                tree.add_node(next_node)
                tree.add_edge(node, next_node)
            i += 1
        time -= dt

    return tree



def main():

    return 



if __name__ == '__main__':
    main()

