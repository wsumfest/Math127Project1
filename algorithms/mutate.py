from numpy import linalg as LA
import numpy as np


class MarkovChain:

    def __init__(self, transition_matrix, time):
        self.transition_matrix = transition_matrix
        self.time = time


    def apply_to_char(self, char):
        assert(char == 'A' or char == 'C' or char == 'T' or char == 'G')
        char_map = {"A": 0, "C": 1, "G": 2, "T": 3}
        index = char_map[char]
        base_vector = [.25, .25, .25, .25] #Assume uniform probability for bases in DNA
        power_matrix = LA.matrix_power(self.transition_matrix, self.time)
        transformation_vector = power_matrix[index]
        new_char = np.random.choice(char_map.keys(), p=transformation_vector)
        return new_char



def mutate(transition_matrix, time, dna_sequence):
    markov_chain = MarkovChain(transition_matrix, time)
    new_seq = map(markov_chain.apply_to_char, dna_sequence)
    return "".join(new_seq)