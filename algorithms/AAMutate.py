from numpy import linalg as LA
import numpy as np
import multiprocessing as mp
from functools import partial
import subprocess


class MarkovChain(object):

    def __init__(self, transition_matrix, time):
        self.transition_matrix = transition_matrix
        self.time = time


    def apply_to_char(self, char):
        assert char in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
        char_map = {'A':0, 'R':1, 'N':2, 'D':3, 'C':4, 'Q':5, 'E':6, 'G':7, 'H':8, 'I':9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, 'T':16, 'W':17, 'Y':18, 'V':19}
        base_vector = [.074, .042, .044, .059, .033, .058, .037, .074, .029, .038, .076, .072, .018, .04, .05, .081, .062, .013, .033, .068] #observed frequencies in vertebrates
        power_matrix = LA.matrix_power(self.transition_matrix, self.time)
        transformation_vector = power_matrix[index]
        new_char = np.random.choice(char_map.keys(), p=transformation_vector)
        return new_char



def mutate(time, aa_sequence):
    #sets maximum number of processes
    proc = subprocess.Popen(["sysctl", "-n", "hw.ncpu"], stdout=subprocess.PIPE)
    #truncate last char == '\n'
    maximum_processes = int(proc.stdout.read()[:-1])
    #Use as Pool of processes for multithreaded programming
    pool = mp.Pool(processes=20)

    transition_matrix = build_transition_matrix()
    markov_chain = MarkovChain(transition_matrix, time)
    my_func = partial(alias, markov_chain=markov_chain)

    #Apply instance method over that dna_sequence with pool.map
    new_seq = pool.map(my_func, aa_sequence)
    return "".join(new_seq)

def build_transition_matrix():
    #frequencies = {0:.074, 1:.042, 2:.059, 3:.058, 4:.04, 5.074, 6:.029, 7:.038, 8:.072, 9:.076, 10:.018, 11:.044, 12:.068, 13:.037, 14:.042, 15:.081, 16:.062, 17:.05, 18:.013, 19:.033}
    vector1 = [0.16, 0.07, 0.08, 0.08, 0.11, 0.08, 0.08, 0.09, 0.06, 0.07, 0.06, 0.08, 0.07, 0.05, 0.10, 0.11, 0.09, 0.04, 0.05, 0.08]
    vector2 = [0.04, 0.16, 0.06, 0.05, 0.04, 0.07, 0.06, 0.04, 0.06, 0.03, 0.03, 0.10, 0.04, 0.03, 0.04, 0.05, 0.05, 0.03, 0.03, 0.03]
    vector3 = [0.04, 0.04, 0.09, 0.06, 0.03, 0.04, 0.05, 0.04, 0.05, 0.02, 0.02, 0.05, 0.02, 0.02, 0.03, 0.05, 0.04, 0.02, 0.03, 0.02]
    vector4 = [0.05, 0.05, 0.10, 0.17, 0.03, 0.07, 0.11, 0.05, 0.06, 0.02, 0.02, 0.07, 0.03, 0.02, 0.05, 0.06, 0.05, 0.02, 0.03, 0.03]
    vector5 = [0.02, 0.01, 0.01, 0.01, 0.12, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.02]
    vector6 = [0.03, 0.05, 0.04, 0.04, 0.02, 0.07, 0.05, 0.02, 0.04, 0.02, 0.02, 0.05, 0.03, 0.02, 0.03, 0.04, 0.03, 0.02, 0.02, 0.02]
    vector7 = [0.07, 0.08, 0.09, 0.13, 0.04, 0.10, 0.15, 0.05, 0.07, 0.03, 0.03, 0.09, 0.04, 0.03, 0.06, 0.07, 0.07, 0.03, 0.04, 0.04]
    vector8 = [0.09, 0.06, 0.09, 0.07, 0.05, 0.06, 0.06, 0.39, 0.05, 0.02, 0.02, 0.06, 0.03, 0.02, 0.05, 0.08, 0.05, 0.03, 0.03, 0.03]
    vector9 = [0.02, 0.02, 0.03, 0.02, 0.01, 0.03, 0.02, 0.01, 0.11, 0.01, 0.01, 0.02, 0.02, 0.03, 0.02, 0.02, 0.02, 0.03, 0.04, 0.01]
    vector10 = [0.05, 0.04, 0.03, 0.02, 0.07, 0.04, 0.03, 0.02, 0.04, 0.17, 0.13, 0.04, 0.12, 0.08, 0.03, 0.04, 0.06, 0.05, 0.05, 0.15]
    vector11 = [0.07, 0.05, 0.04, 0.03, 0.08, 0.06, 0.04, 0.03, 0.06, 0.17, 0.22, 0.05, 0.18, 0.14, 0.05, 0.05, 0.07, 0.08, 0.09, 0.14]
    vector12 = [0.06, 0.13, 0.08, 0.07, 0.04, 0.10, 0.09, 0.05, 0.08, 0.04, 0.04, 0.14, 0.05, 0.03, 0.05, 0.07, 0.06, 0.03, 0.04, 0.04]
    vector13 = [0.02, 0.02, 0.01, 0.01, 0.02, 0.02, 0.01, 0.01, 0.02, 0.04, 0.05, 0.02, 0.06, 0.03, 0.01, 0.02, 0.02, 0.02, 0.02, 0.03]
    vector14 = [0.02, 0.02, 0.02, 0.01, 0.04, 0.02, 0.01, 0.01, 0.05, 0.05, 0.06, 0.02, 0.06, 0.20, 0.02, 0.02, 0.02, 0.12, 0.15, 0.04]
    vector15 = [0.05, 0.03, 0.03, 0.03, 0.02, 0.03, 0.04, 0.02, 0.04, 0.02, 0.02, 0.03, 0.02, 0.02, 0.29, 0.05, 0.03, 0.01, 0.02, 0.02]
    vector16 = [0.07, 0.06, 0.07, 0.06, 0.07, 0.06, 0.06, 0.06, 0.05, 0.03, 0.03, 0.06, 0.04, 0.03, 0.06, 0.10, 0.08, 0.03, 0.03, 0.04]
    vector17 = [0.06, 0.05, 0.06, 0.05, 0.07, 0.06, 0.06, 0.04, 0.05, 0.05, 0.04, 0.06, 0.05, 0.04, 0.05, 0.08, 0.12, 0.03, 0.04, 0.06]
    vector18 = [0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.00, 0.01, 0.03, 0.00, 0.01, 0.00, 0.26, 0.03, 0.01]
    vector19 = [0.02, 0.02, 0.02, 0.01, 0.03, 0.02, 0.01, 0.01, 0.06, 0.02, 0.03, 0.02, 0.03, 0.11, 0.01, 0.02, 0.02, 0.10, 0.19, 0.02]
    vector20 = [0.07, 0.04, 0.04, 0.03, 0.10, 0.05, 0.04, 0.03, 0.04, 0.17, 0.12, 0.05, 0.11, 0.08, 0.04, 0.06, 0.08, 0.05, 0.06, 0.18]
    transition_matrix = [vector1, vector2, vector3, vector4, vector5, vector6, vector7, vector8, vector9, vector10, vector11, vector12, vector13, vector14, vector15, vector16, vector17, vector18, vector19, vector20]
    return transition_matrix


#Alias function that allows instance method for markov chain to be pickled for multiprocessing
def alias(arg, markov_chain):
    return markov_chain.apply_to_char(arg)