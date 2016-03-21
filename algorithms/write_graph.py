import mutate
import test_evolution_simulaton




def main():

    output_file = open("../graphs/output_graph.gv", "a")
    bens_file = open("../bens_file.txt", "a")

    tree = test_evolution_simulaton.main()
    
    edges = tree.get_edges()
    node_hash = {}


    output_file.write('digraph finite_state_machine {\n')
    output_file.write('    rankdir=LR;\n')
    output_file.write('    size="8,5"\n')
    output_file.write('    node [shape = circle];\n')

    n = 1
    for edge in edges:
        if edge[0] not in node_hash:
            node_hash[edge[0]] = edge[0]
        edge_1 = node_hash[edge[0]]
        if edge[1] not in node_hash:
            node_hash[edge[1]] = edge[1]
        edge_2 = node_hash[edge[1]]

        bens_file.write("Node_" + str(edge_1) + ":" + str("".join(edge_1.get_sequence())) + "\n")
        bens_file.write("Node_" + str(edge_2) + ":" + str("".join(edge_2.get_sequence())) + "\n")

        output_file.write('     ' + 'Node_' + str(edge_1) +  ' -> Node_' + str(edge_2) + ' [ label = ' + str(edge[2]) + '];\n') 

    output_file.write("}")









if __name__ == '__main__':
    main()